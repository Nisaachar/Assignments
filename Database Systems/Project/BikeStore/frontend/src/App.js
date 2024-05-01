import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import MostSoldProduct from './MostSoldProduct';
import TopProducts from './TopProducts';
import CreateOrderForm from './CreateOrderForm';
import Dashboard from './Dashboard'; 
import UpdateOrderStatus from './UpdateOrderStatus'


function App() {
  return (
    <Router>
      <div style={{ padding: 20 }}>
        <nav style={{ marginBottom: 20 }}>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            <li style={{ display: 'inline', marginRight: 10 }}><Link to="/dashboard">Dashboard</Link></li>
            <li style={{ display: 'inline', marginRight: 10 }}><Link to="/top-products">Top N Products</Link></li>
            <li style={{ display: 'inline', marginRight: 10 }}><Link to="/create-order-form">Create Order</Link></li>
            <li style={{ display: 'inline', marginRight: 10 }}><Link to="/UpdateOrderStatus">Update Order</Link></li>
          </ul>
        </nav>

        {/* Route setup for different pages */}
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/most-sold-product" element={<MostSoldProduct />} />
          <Route path="/top-products" element={<TopProducts />} />
          <Route path="/create-order-form" element={<CreateOrderForm />} />
          <Route path ="/UpdateOrderStatus" element={<UpdateOrderStatus /> } />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
