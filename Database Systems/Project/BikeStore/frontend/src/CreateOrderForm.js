import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Grid, Typography, Box } from '@mui/material';

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
        <Container maxWidth="sm">
            <Typography variant="h6" gutterBottom>
                Create New Order
            </Typography>
            <Box border={1} borderColor="grey.500" borderRadius={2} p={3}>
                <form onSubmit={handleSubmit}>
                    <Grid container spacing={3}>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="Order ID"
                                name="order_id"
                                value={orderData.order_id}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="Order Status"
                                name="order_status"
                                value={orderData.order_status}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                type="date"
                                label="Order Date"
                                name="order_date"
                                value={orderData.order_date}
                                onChange={handleChange}
                                InputLabelProps={{
                                    shrink: true,
                                }}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                type="date"
                                label="Required Date"
                                name="required_date"
                                value={orderData.required_date}
                                onChange={handleChange}
                                InputLabelProps={{
                                    shrink: true,
                                }}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                type="date"
                                label="Shipped Date"
                                name="shipped_date"
                                value={orderData.shipped_date}
                                onChange={handleChange}
                                InputLabelProps={{
                                    shrink: true,
                                }}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <Button variant="contained" color="primary" type="submit">
                                Create Order
                            </Button>
                        </Grid>
                    </Grid>
                </form>
            </Box>
        </Container>
    );
}

export default CreateOrderForm;
