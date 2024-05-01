import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Typography } from '@mui/material';

function UpdateOrderStatus() {
    const [orderId, setOrderId] = useState('');
    const [newStatus, setNewStatus] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:5001/api/update-order-status', {
                order_id: orderId,
                new_status: newStatus
            });
            setMessage(response.data.message);
        } catch (error) {
            if (error.response && error.response.status === 404) {
                setMessage('Node not found');
            } else {
                setMessage('Failed to update order status');
            }
        }
    };

    return (
        <div>
            <Typography variant="h6">Update Order Status</Typography>
            <form onSubmit={handleSubmit}>
                <TextField
                    label="Order ID"
                    value={orderId}
                    onChange={e => setOrderId(e.target.value)}
                    required
                />
                <TextField
                    label="New Status"
                    value={newStatus}
                    onChange={e => setNewStatus(e.target.value)}
                    required
                />
                <Button type="submit" variant="contained" color="primary">Update Status</Button>
            </form>
            {message && <Typography>{message}</Typography>}
        </div>
    );
}

export default UpdateOrderStatus;
