import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function TotalOrders() {
    const [totalOrders, setTotalOrders] = useState('Loading...');

    useEffect(() => {
        axios.get('http://localhost:5001/api/total-orders')
            .then(response => {
                setTotalOrders(response.data.TotalOrders);
            })
            .catch(error => {
                console.error('Error fetching total orders:', error);
                setTotalOrders('Failed to fetch data');
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Total Orders
                </Typography>
                <Typography variant="h5" component="div">
                    {totalOrders}
                </Typography>
            </CardContent>
        </Card>
    );
}

export default TotalOrders;
