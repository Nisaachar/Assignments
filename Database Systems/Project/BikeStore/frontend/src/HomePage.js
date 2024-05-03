import React from 'react';
import { Box, Grid, Typography } from '@mui/material';
import RevenueTrend from './RevenueTrend';
import ActiveCustomers from './ActiveCustomers';
import TotalSalesRevenue from './TotalSalesRevenue';


function HomePage() {
    return (
        // Outer Box to center the content and set a max width
        <Box display="flex" justifyContent="center" alignItems="center">
            <Box width="80em" padding={3} boxShadow={3} bgcolor="background.paper">
                <Typography variant="h4" gutterBottom>Welcome to the Bike Store Dashboard</Typography>
                <Grid container spacing={2} direction="column">
                    <Grid item>
                        <TotalSalesRevenue />
                    </Grid>
                    <Grid item>
                        <ActiveCustomers />
                    </Grid>
                    <Grid item>
                        <RevenueTrend />
                    </Grid>
                </Grid>
            </Box>
        </Box>
    );
}

export default HomePage;