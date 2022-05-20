import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
const TestRun = () => {

  let [FDA, setFDA] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    
      getFDA();
  
  }, []);

  let getFDA = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/fda_filtered_sheets/`
    );
    let data = await response.json();

    console.log(data);
    setFDA(data);
    setLoading(false);
  };
  return (
    <div>
     </div>
)};

export default TestRun;
