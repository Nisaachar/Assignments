import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function TotalSalesRevenue() {
    const [salesRevenue, setSalesRevenue] = useState('Loading...');

    useEffect(() => {
        axios.get('http://localhost:5001/api/total-sales-revenue')
            .then(response => {
                // Assuming the backend returns data as a number
                setSalesRevenue(`$${response.data.TotalSalesRevenue.toFixed(2)}`);
            })
            .catch(error => {
                console.error('Error fetching total sales revenue:', error);
                setSalesRevenue('Failed to fetch data');
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Total Sales Revenue
                </Typography>
                <Typography variant="h5" component="div">
                    {salesRevenue}
                </Typography>
            </CardContent>
        </Card>
    );
}

export default TotalSalesRevenue;
