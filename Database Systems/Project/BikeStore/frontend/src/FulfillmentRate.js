import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function FulfillmentRate() {
    const [rate, setRate] = useState({
        OrdersOnTime: 'Loading...',
        FulfillmentRate: 0
    });

    useEffect(() => {
        axios.get('http://localhost:5001/api/fulfillment-rate')
            .then(response => {
                setRate({
                    OrdersOnTime: response.data.OrdersOnTime,
                    FulfillmentRate: response.data.FulfillmentRate.toFixed(2)
                });
            })
            .catch(error => {
                console.error('Error fetching fulfillment rate:', error);
                setRate({ OrdersOnTime: 'Failed to fetch data', FulfillmentRate: 0 });
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Fulfillment Rate
                </Typography>
                <Typography variant="h5" component="div">
                    {`${rate.FulfillmentRate}%`}
                </Typography>
                <Typography color="text.secondary">
                    Orders on Time: {rate.OrdersOnTime}
                </Typography>
            </CardContent>
        </Card>
    );
}

export default FulfillmentRate;
