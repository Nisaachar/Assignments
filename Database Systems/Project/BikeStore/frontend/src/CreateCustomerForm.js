import React, { useState } from 'react';
import axios from 'axios';
import { TextField, Button, Container, Grid, Typography, Box } from '@mui/material';

function CreateCustomerForm() {
    const [customerData, setCustomerData] = useState({
        customer_id: '',  // Added customer_id to the state
        first_name: '',
        last_name: '',
        phone: '',
        email: '',
        street: '',
        city: '',
        state: '',
        zip_code: ''
    });

    const handleChange = (e) => {
        setCustomerData({ ...customerData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:5001/api/customers', customerData)
            .then(response => {
                alert('Customer created successfully!');
                console.log(response.data);
            })
            .catch(error => {
                alert('Failed to create customer');
                console.error('There was an error!', error);
            });
    };

    return (
        <Container maxWidth="sm">
            <Typography variant="h6" gutterBottom>
                Create New Customer
            </Typography>
            <Box border={1} borderColor="grey.400" borderRadius={2} p={3}>
                <form onSubmit={handleSubmit}>
                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="Customer ID"
                                name="customer_id"
                                value={customerData.customer_id}
                                onChange={handleChange}
                                variant="outlined"
                                type="number"  
                            />
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                fullWidth
                                label="First Name"
                                name="first_name"
                                value={customerData.first_name}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                fullWidth
                                label="Last Name"
                                name="last_name"
                                value={customerData.last_name}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="Phone"
                                name="phone"
                                value={customerData.phone}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="Email"
                                name="email"
                                value={customerData.email}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="Street"
                                name="street"
                                value={customerData.street}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                fullWidth
                                label="City"
                                name="city"
                                value={customerData.city}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <TextField
                                fullWidth
                                label="State"
                                name="state"
                                value={customerData.state}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                label="Zip Code"
                                name="zip_code"
                                type="number"
                                value={customerData.zip_code}
                                onChange={handleChange}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <Button type="submit" variant="contained" color="primary">
                                Create Customer
                            </Button>
                        </Grid>
                    </Grid>
                </form>
            </Box>
        </Container>
    );
}

export default CreateCustomerForm;
