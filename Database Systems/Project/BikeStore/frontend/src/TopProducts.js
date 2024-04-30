import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TopProducts() {
    const [topProducts, setTopProducts] = useState([]);
    const [topLimit, setTopLimit] = useState(10);  // Default to top 10

    useEffect(() => {
        axios.get(`http://localhost:5001/api/top-products?top=${topLimit}`)
            .then(response => {
                setTopProducts(response.data);
            })
            .catch(error => {
                console.error('Error fetching top products', error);
            });
    }, [topLimit]);  // Rerun when topLimit changes

    return (
        <div>
            <h2>Top Products</h2>
            <select value={topLimit} onChange={(e) => setTopLimit(e.target.value)}>
                <option value="5">Top 5</option>
                <option value="10">Top 10</option>
                <option value="20">Top 20</option>
            </select>
            <ul>
                {topProducts.map((product, index) => (
                    <li key={index}>{product.Product}: ${product.TotalSales}</li>
                ))}
            </ul>
        </div>
    );
}

export default TopProducts;
