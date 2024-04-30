import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MostSoldProduct() {
  const [productInfo, setProductInfo] = useState('Loading...');

  useEffect(() => {
    axios.get('http://localhost:5001/api/most-sold-product')
         .then(response => {
           const { product, quantity } = response.data;
           setProductInfo(`Most Sold Product: ${product} (Quantity: ${quantity})`);
         })
         .catch(error => {
           console.error('Error fetching data:', error);
           setProductInfo('Failed to fetch data');
         });
  }, []);

  return <h1>{productInfo}</h1>;
}

export default MostSoldProduct;
