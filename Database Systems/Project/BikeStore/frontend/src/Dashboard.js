import React from 'react';
import { Grid } from '@mui/material';
import MostSoldProduct from './MostSoldProduct';
import AverageOrderPrice from './AverageOrderPrice';
import TotalOrders from './TotalOrders';
import TotalSalesRevenue from './TotalSalesRevenue';
import ActiveCustomers from './ActiveCustomers';
import TotalCustomers from './TotalCustomers';
import SalesByCity from './SalesByCity';
import EmployeeOfTheYear from './EmployeeOfTheYear'; 
import FulfillmentRate  from './FulfillmentRate';
import RevenueTrend from './RevenueTrend';

function Dashboard() {
    return (
        <div>
            <h1>Dashboard</h1>
            <Grid container spacing={2}>
                <Grid item xs={3}>
                    <MostSoldProduct />
                </Grid>
                <Grid item xs={3}>
                    <AverageOrderPrice />
                </Grid>
                <Grid item xs={3}>
                    <TotalOrders />
                </Grid>
                <Grid item xs={3}>
                    <TotalSalesRevenue />
                </Grid>
                <Grid item xs={3}>
                    <ActiveCustomers />
                </Grid>
                <Grid item xs={3}>
                    <TotalCustomers />
                </Grid>
                <Grid item xs={3}>
                    <SalesByCity />
                </Grid>
                <Grid item xs={3}>
                    <EmployeeOfTheYear />
                </Grid>
                <Grid item xs={3}>
                    <FulfillmentRate />
                </Grid>
                <Grid item xs={6}>
                    <RevenueTrend /> 
                </Grid>
            </Grid>
        </div>
    );
}

export default Dashboard;
