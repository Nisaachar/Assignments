import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';


function AverageOrderPrice() {
    const [averagePrice, setAveragePrice] = useState('Loading...');

    useEffect(() => {
        axios.get('http://localhost:5001/api/average-order-price')
            .then(response => {
                setAveragePrice(`$${response.data.AverageOrderValue.toFixed(2)}`);
            })
            .catch(error => {
                console.error('Error fetching average order price:', error);
                setAveragePrice('Failed to fetch data');
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Average Order Price
                </Typography>
                <Typography variant="h5" component="div">
                    {averagePrice}
                </Typography>
            </CardContent>
        </Card>
    );
}

export default AverageOrderPrice;

