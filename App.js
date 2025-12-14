import React, { useEffect, useState } from "react";
import api from "./api";

function App() {
  const [sweets, setSweets] = useState([]);

  useEffect(() => {
    api.get("/api/sweets")
      .then(res => setSweets(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Sweet Shop</h1>
      {sweets.map(sweet => (
        <div key={sweet.id}>
          <h3>{sweet.name}</h3>
          <p>Category: {sweet.category}</p>
          <p>Price: ₹{sweet.price}</p>
          <p>Quantity: {sweet.quantity}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default App;
