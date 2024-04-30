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
    CREATE (order:Order {
        order_id: $order_id,
        order_status: $order_status,
        order_date: date($order_date),
        required_date: date($required_date),
        shipped_date: date($shipped_date)
    })
    RETURN order
    """

    with driver.session() as session:
        result = session.run(query, data)
        created_order = result.single()

    if created_order:
        # Convert Neo4j Node to a dictionary and handle dates
        order_dict = {k: (created_order['order'][k].to_native() if isinstance(created_order['order'][k], time.Date) else created_order['order'][k]) for k in created_order['order'].keys()}
        return jsonify(order_dict)
    else:
        return jsonify({'error': 'Failed to create order'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
   # order_date: date($order_date),
        # required_date: date($required_date),
        # shipped_date: date($shipped_date)