import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import 'chart.js/auto';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function RevenueTrend() {
    const [chartData, setChartData] = useState({
        labels: [],
        datasets: [
            {
                label: 'Monthly Revenue',
                data: [],
                borderColor: 'rgb(75, 192, 192)',
                backgroundColor: 'rgba(75, 192, 192, 0.5)',
            }
        ]
    });

    const fetchData = async () => {
        try {
            const response = await axios.get('http://localhost:5001/api/revenue-trend');
            const data = response.data;
            const labels = data.map(item => item.Month.substring(0, 7)); // Simplify date format
            const dataset = data.map(item => item.MonthlyRevenue);

            setChartData(prevState => ({
                ...prevState,
                labels: labels,
                datasets: [
                    {
                        ...prevState.datasets[0],
                        data: dataset
                    }
                ]
            }));
        } catch (error) {
            console.error('Error fetching revenue trend data:', error);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Revenue Trend Over Time
                </Typography>
                <Line data={chartData} options={{ responsive: true, scales: { y: { beginAtZero: true } } }} />
            </CardContent>
        </Card>
    );
}

export default RevenueTrend;
