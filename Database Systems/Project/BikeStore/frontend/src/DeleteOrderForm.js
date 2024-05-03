import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Box } from '@mui/material';

function DeleteOrderForm() {
    const [orderId, setOrderId] = useState('');

    const handleDelete = () => {
        if (!orderId) {
            alert('Please enter a valid Order ID');
            return;
        }
        axios.delete(`http://localhost:5001/api/delete-order/${orderId}`)
            .then(response => {
                alert('Order deleted successfully');
                setOrderId('');  // Clear the input after successful deletion
            })
            .catch(error => {
                alert('Failed to delete order');
                console.error('Error:', error);
            });
    };

    return (
        <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center">
            <TextField
                label="Order ID"
                variant="outlined"
                value={orderId}
                onChange={e => setOrderId(e.target.value)}
                sx={{ marginBottom: 2 }}
            />
            <Button variant="contained" color="primary" onClick={handleDelete}>
                Delete Order
            </Button>
        </Box>
    );
}

export default DeleteOrderForm;
