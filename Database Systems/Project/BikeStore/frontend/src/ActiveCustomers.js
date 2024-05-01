import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function ActiveCustomers() {
    const [activeCustomers, setActiveCustomers] = useState('Loading...');

    useEffect(() => {
        axios.get('http://localhost:5001/api/active-customers')
            .then(response => {
                setActiveCustomers(response.data.ActiveCustomers);
            })
            .catch(error => {
                console.error('Error fetching active customers:', error);
                setActiveCustomers('Failed to fetch data');
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Active Customers
                </Typography>
                <Typography variant="h5" component="div">
                    {activeCustomers}
                </Typography>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    (Users who placed orders after the year 2018)
                </Typography>
            </CardContent>
        </Card>
    );
}

export default ActiveCustomers;
