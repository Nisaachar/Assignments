import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function EmployeeOfTheYear() {
    const [employee, setEmployee] = useState({
        FirstName: 'Loading...',
        LastName: ''
    });

    useEffect(() => {
        axios.get('http://localhost:5001/api/employee-of-the-year')
            .then(response => {
                setEmployee({
                    FirstName: response.data.FirstName,
                    LastName: response.data.LastName
                });
            })
            .catch(error => {
                console.error('Error fetching Employee of the Year:', error);
                setEmployee({ FirstName: 'Failed to fetch data', LastName: '' });
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Employee of the Year
                </Typography>
                <Typography variant="h5" component="div">
                    {`${employee.FirstName} ${employee.LastName}`}
                </Typography>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    (By sales)
                </Typography>
            </CardContent>
        </Card>
    );
}

export default EmployeeOfTheYear;
