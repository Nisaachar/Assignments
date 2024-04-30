import React, { useState } from 'react';
import axios from 'axios';

function CreateOrderForm() {
    const [orderData, setOrderData] = useState({
        order_id: '',
        order_status: '',
        order_date: '',
        required_date: '',
        shipped_date: ''
    });

    const handleChange = (e) => {
        setOrderData({ ...orderData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:5001/api/orders', orderData)
            .then(response => {
                alert('Order created successfully!');
                console.log(response.data);
            })
            .catch(error => {
                alert('Failed to create order');
                console.error('There was an error!', error);
            });
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Order ID:
                <input type="text" name="order_id" value={orderData.order_id} onChange={handleChange} />
            </label>
            <label>
                Order Status:
                <input type="text" name="order_status" value={orderData.order_status} onChange={handleChange} />
            </label>
            <label>
                Order Date:
                <input type="date" name="order_date" value={orderData.order_date} onChange={handleChange} />
            </label>
            <label>
                Required Date:
                <input type="date" name="required_date" value={orderData.required_date} onChange={handleChange} />
            </label>
            <label>
                Shipped Date:
                <input type="date" name="shipped_date" value={orderData.shipped_date} onChange={handleChange} />
            </label>
            <button type="submit">Create Order</button>
        </form>
    );
}

export default CreateOrderForm;
