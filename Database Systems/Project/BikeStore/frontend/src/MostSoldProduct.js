// import React, { useState, useEffect } from 'react';
// import axios from 'axios';

// function MostSoldProduct() {
//   const [productInfo, setProductInfo] = useState({ product: 'Loading...', quantity: 0 });

//   useEffect(() => {
//     axios.get('http://localhost:5001/api/most-sold-product')
//          .then(response => {
//            const { product, quantity } = response.data;
//            setProductInfo({ product, quantity });
//          })
//          .catch(error => {
//            console.error('Error fetching data:', error);
//            setProductInfo({ product: 'Failed to fetch data', quantity: 0 });
//          });
//   }, []);

//   return (
//     <div className="card">
//       <h2>Most Sold Product</h2>
//       <div className="card-content">
//         <p>Product: <strong>{productInfo.product}</strong></p>
//         <p>Quantity Sold: <strong>{productInfo.quantity}</strong></p>
//       </div>
//     </div>
//   );
// }

// export default MostSoldProduct;


import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

function MostSoldProduct() {
    const [productInfo, setProductInfo] = useState({ product: 'Loading...', quantity: 0 });

    useEffect(() => {
        axios.get('http://localhost:5001/api/most-sold-product')
            .then(response => {
                const { product, quantity } = response.data;
                setProductInfo({ product, quantity });
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setProductInfo({ product: 'Failed to fetch data', quantity: 0 });
            });
    }, []);

    return (
        <Card variant="outlined" sx={{ minWidth: 275, borderColor: '#007bff', borderWidth: 2 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Most Sold Product
                </Typography>
                <Typography variant="h5" component="div">
                    {productInfo.product}
                </Typography>
                <Typography sx={{ mb: 1.5 }} color="text.secondary">
                    Quantity Sold: {productInfo.quantity}
                </Typography>
            </CardContent>
        </Card>
    );
}

export default MostSoldProduct;

