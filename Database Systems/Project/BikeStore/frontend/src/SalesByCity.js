import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableRow from '@mui/material/TableRow';
import TableCell from '@mui/material/TableCell';

function SalesByCity() {
    const [salesData, setSalesData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5001/api/sales-by-city')
            .then(response => {
                setSalesData(response.data);
            })
            .catch(error => {
                console.error('Error fetching sales by city:', error);
                setSalesData([]);
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Sales by City
                </Typography>
                <Table size="small">
                    <TableBody>
                        {salesData.map((item, index) => (
                            <TableRow key={index}>
                                <TableCell component="th" scope="row">
                                    {item.Location}
                                </TableCell>
                                <TableCell align="right">
                                    ${item.TotalSales.toFixed(2)}
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </CardContent>
        </Card>
    );
}

export default SalesByCity;
