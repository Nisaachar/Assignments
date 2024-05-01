from flask import Flask, jsonify, request  
from neo4j import GraphDatabase
from flask_cors import CORS
import os
from neo4j import GraphDatabase, time

app = Flask(__name__)
CORS(app)

# Setup Neo4j connection
uri = "neo4j://localhost:7687"  # Your Neo4j host (update if different)
db_username = "neo4j"           # Default Neo4j username
db_password = "English%15@"        # Update with your Neo4j password

driver = GraphDatabase.driver(uri, auth=(db_username, db_password))

def get_db():
    return driver.session()

@app.route('/')
def hello_world():
    return 'Hello, Welcome to the Bike Store Dashboarding!'

@app.route('/api/test')
def test_neo4j():
    session = get_db()
    result = session.run("MATCH (n) RETURN count(n) as num")
    count = result.single()["num"]
    session.close()
    return f"Number of nodes in Neo4j: {count}"

@app.route('/api/most-sold-product')
def get_most_sold_product():
    session = get_db()
    query = """
        MATCH (p:Product)<-[:PRODUCT]-(oi:OrderItem)
        WITH p, sum(oi.quantity) AS total_quantity
        ORDER BY total_quantity DESC
        LIMIT 1
        RETURN p.product_name AS product, total_quantity
    """
    result = session.run(query)
    record = result.single()
    session.close()
    if record:
        return jsonify({
            'product': record['product'],
            'quantity': record['total_quantity']
        })
    else:
        return jsonify({'error': 'No data found'})

# get the top n

@app.route('/api/top-products', methods=['GET'])
def get_top_products():
    top_limit = request.args.get('top', default=10, type=int)  # Get the top limit from query parameter

    query = """
    MATCH (order:Order)
    WITH min(order.order_date) AS MinDate, max(order.order_date) AS MaxDate
    MATCH (product:Product)<-[r:PRODUCT]-(item:OrderItem), (order)-[:PART_OF]-(item)
    WHERE order.order_date >= MinDate AND order.order_date <= MaxDate
    RETURN product.product_name AS Product, sum(item.quantity * item.list_price) AS TotalSales
    ORDER BY TotalSales DESC
    LIMIT $top_limit
    """

    with driver.session() as session:
        result = session.run(query, {"top_limit": top_limit})
        products = [{"Product": record["Product"], "TotalSales": record["TotalSales"]} for record in result]

    return jsonify(products)

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    order_id = data['order_id']
    order_status = data['order_status']
    order_date = data['order_date']
    required_date = data['required_date']
    shipped_date = data['shipped_date']

    query = """
    MATCH (defaultItem:OrderItem {id: 9999})  
    CREATE (order:Order {
        order_id: $order_id,
        order_status: $order_status,
        order_date: date($order_date),
        required_date: date($required_date),
        shipped_date: date($shipped_date)
    })
    CREATE (order)-[:CONTAINS]->(defaultItem)
    RETURN order, defaultItem
    """

    with driver.session() as session:
        result = session.run(query, data)
        created_order = result.single()

    if created_order:
        # Convert Neo4j Node to a dictionary and handle dates
        order_dict = {
            'order': {k: (created_order['order'][k].to_native() if isinstance(created_order['order'][k], time.Date) else created_order['order'][k]) for k in created_order['order'].keys()},
            'order_item': {k: created_order['defaultItem'][k] for k in created_order['defaultItem'].keys()}
        }
        return jsonify(order_dict)
    else:
        return jsonify({'error': 'Failed to create order'}), 400


@app.route('/api/average-order-price')
def get_average_order_price():
    query = "MATCH (o:OrderItem) RETURN avg(o.list_price) AS AverageOrderPrice"
    
    with driver.session() as session:
        result = session.run(query)
        record = result.single()  # Store the result in a variable

        if record:
            average_price = record[0]  # Access the first (and only) element if record is not None
            return jsonify({'AverageOrderValue': average_price})
        else:
            return jsonify({'error': 'No data found'}), 404

@app.route('/api/total-orders')
def get_total_orders():
    query = "MATCH (o:Order) RETURN count(o) AS TotalOrders"
    with driver.session() as session:
        result = session.run(query)
        record = result.single()  # Fetch the result once

        if record:
            total_orders = record[0]  # Safely access the result
        else:
            total_orders = 0  # Default to 0 if no record is found

    return jsonify({'TotalOrders': total_orders})

@app.route('/api/total-sales-revenue')
def get_total_sales_revenue():
    query = """
    MATCH (o:OrderItem)
    RETURN round(100 * sum(o.list_price)) / 100 AS TotalSalesRevenue
    """
    with driver.session() as session:
        result = session.run(query)
        record = result.single()  # Fetch the result once

        if record:
            total_sales_revenue = record["TotalSalesRevenue"]  # Access the rounded result
        else:
            total_sales_revenue = 0  # Default to 0 if no record is found

    return jsonify({'TotalSalesRevenue': total_sales_revenue})

@app.route('/api/active-customers')
def get_active_customers():
    query = """
    MATCH (c:Customer)-[:PLACED_BY]-(o:Order)
    WHERE o.order_date >= date('2018-01-01')
    WITH DISTINCT c
    RETURN count(c) AS ActiveCustomers
    """
    with driver.session() as session:
        result = session.run(query)
        record = result.single()  # Fetch the result once

        if record:
            active_customers = record["ActiveCustomers"]  # Access the result
        else:
            active_customers = 0  # Default to 0 if no record is found

    return jsonify({'ActiveCustomers': active_customers})

@app.route('/api/total-customers')
def get_total_customers():
    query = """
    MATCH (c:Customer)
    RETURN count(DISTINCT c) AS TotalCustomers
    """
    with driver.session() as session:
        result = session.run(query)
        record = result.single()  # Fetch the result once

        if record:
            total_customers = record["TotalCustomers"]  # Access the result
        else:
            total_customers = 0  # Default to 0 if no record is found

    return jsonify({'TotalCustomers': total_customers})

@app.route('/api/sales-by-city')
def get_sales_by_city():
    query = """
    MATCH (s:Store)-[:FULFILLED_BY]-(o:Order)-[:PART_OF]-(oi:OrderItem)
    WITH s, sum(oi.list_price) AS TotalSales
    RETURN s.city AS Location, TotalSales
    ORDER BY TotalSales DESC
    """
    with driver.session() as session:
        result = session.run(query)
        sales_by_city = [{"Location": record["Location"], "TotalSales": record["TotalSales"]} for record in result]

    return jsonify(sales_by_city)

@app.route('/api/employee-of-the-year')
def get_employee_of_the_year():
    query = """
    MATCH (st:Staff)-[:PLACED_BY]-(o:Order)-[:CONTAINS]-(oi:OrderItem)
    RETURN st.first_name AS FirstName, st.last_name AS LastName, sum(oi.list_price) AS TotalSales
    ORDER BY TotalSales DESC
    LIMIT 1
    """
    with driver.session() as session:
        result = session.run(query)
        record = result.single()  # Fetch the result once

        if record:
            employee = {
                "FirstName": record["FirstName"],
                "LastName": record["LastName"],
                "TotalSales": record["TotalSales"]
            }
        else:
            employee = {"FirstName": "No data", "LastName": "", "TotalSales": 0}

    return jsonify(employee)

@app.route('/api/fulfillment-rate')
def get_fulfillment_rate():
    query = """
    MATCH (o:Order)
    WITH count(o) AS TotalOrders
    MATCH (o:Order)
    WHERE o.shipped_date <= o.required_date
    WITH count(o) AS OrdersOnTime, TotalOrders
    RETURN OrdersOnTime, OrdersOnTime * 100.0 / TotalOrders AS FulfillmentRate
    """
    with driver.session() as session:
        result = session.run(query)
        record = result.single()  # Fetch the result once

        if record:
            fulfillment_rate = {
                "OrdersOnTime": record["OrdersOnTime"],
                "FulfillmentRate": record["FulfillmentRate"]
            }
        else:
            fulfillment_rate = {"OrdersOnTime": 0, "FulfillmentRate": 0.0}

    return jsonify(fulfillment_rate)

@app.route('/api/revenue-trend')
def get_revenue_trend():
    query = """
    MATCH (o:Order)-[:PART_OF]-(oi:OrderItem)
    WHERE o.order_date IS NOT NULL
    RETURN date.truncate('month', date(o.order_date)) AS Month, sum(oi.list_price) AS MonthlyRevenue
    ORDER BY Month
    """
    with driver.session() as session:
        result = session.run(query)
        data = [{"Month": record["Month"].isoformat(), "MonthlyRevenue": record["MonthlyRevenue"]} for record in result]

    return jsonify(data)


@app.route('/api/update-order-status', methods=['POST'])
def update_order_status():
    data = request.json
    try:
        # Convert order_id to integer
        order_id = int(data['order_id'])
        new_status = data['new_status']
    except ValueError:
        return jsonify({'error': 'Invalid order ID format'}), 400

    with driver.session() as session:
        # First, check if the order exists
        order_exists = session.run("""
            MATCH (o:Order {order_id: $order_id})
            RETURN o
        """, {"order_id": order_id}).single()

        if not order_exists:
            return jsonify({'error': 'Node not found'}), 404

        # Update the order status if it exists
        result = session.run("""
            MATCH (o:Order {order_id: $order_id})
            SET o.order_status = $new_status
            RETURN o.order_status AS updated_status
        """, {"order_id": order_id, "new_status": new_status})
        
        updated_status = result.single()["updated_status"]
        return jsonify({'message': 'Order status updated', 'order_status': updated_status})


if __name__ == '__main__':
    app.run(debug=True, port=5001)