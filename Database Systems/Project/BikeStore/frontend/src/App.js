import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import MostSoldProduct from './MostSoldProduct';
import TopProducts from './TopProducts';
import CreateOrderForm from './CreateOrderForm';
import Dashboard from './Dashboard';
import UpdateOrderStatus from './UpdateOrderStatus';
import CreateCustomerForm from './CreateCustomerForm';
import HomePage from './HomePage';
import DeleteOrderForm from './DeleteOrderForm'

function App() {
  return (
    <Router>
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            <Button color="inherit" component={Link} to="/">Bike Store</Button>
          
            </Typography>
            <Button color="inherit" component={Link} to="/dashboard">Dashboard</Button>

            <Button color="inherit" component={Link} to="/top-products">Top N Products</Button>
            <Button color="inherit" component={Link} to="/create-order-form">Create Order</Button>
            <Button color="inherit" component={Link} to="/UpdateOrderStatus">Update Order</Button>
            <Button color="inherit" component={Link} to="/CreateCustomerForm">Create Customer</Button>
            <Button color="inherit" component={Link} to="/DeleteOrderForm">Delete Order</Button>
          </Toolbar>
        </AppBar>
      </Box>
      {/* <HomePage /> */}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/most-sold-product" element={<MostSoldProduct />} />
        <Route path="/top-products" element={<TopProducts />} />
        <Route path="/create-order-form" element={<CreateOrderForm />} />
        <Route path="/UpdateOrderStatus" element={<UpdateOrderStatus />} />
        <Route path="/CreateCustomerForm" element={<CreateCustomerForm />} />
        <Route path="/DeleteOrderForm" element={<DeleteOrderForm />} />
      </Routes>
    </Router>


  );
}

export default App;
