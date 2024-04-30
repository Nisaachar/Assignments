import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import MostSoldProduct from './MostSoldProduct';
import TopProducts from './TopProducts';
import CreateOrderForm from './CreateOrderForm';

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/most-sold-product">Most Sold Product</Link>
            </li>
            <li>
              <Link to="/top-products">Top Products</Link>
            </li>
            <li>
              <Link to="/create-order-form">Create Order</Link> 
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/most-sold-product" element={<MostSoldProduct />} />
          <Route path="/top-products" element={<TopProducts />} />
          <Route path="/create-order-form" element={<CreateOrderForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
