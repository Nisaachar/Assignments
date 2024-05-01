import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function TotalCustomers() {
    const [totalCustomers, setTotalCustomers] = useState('Loading...');

    useEffect(() => {
        axios.get('http://localhost:5001/api/total-customers')
            .then(response => {
                setTotalCustomers(response.data.TotalCustomers);
            })
            .catch(error => {
                console.error('Error fetching total customers:', error);
                setTotalCustomers('Failed to fetch data');
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Total Customers
                </Typography>
                <Typography variant="h5" component="div">
                    {totalCustomers}
                </Typography>
            </CardContent>
        </Card>
    );
}

export default TotalCustomers;
