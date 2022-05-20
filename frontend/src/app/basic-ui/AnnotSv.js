import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

toast.configure();
const AnnotSV = () => {
  let [Annotsv, setAnnotsv] = useState([]);

  useEffect(() => {
    setInterval(function () {
      getanalysis();
    }, 900000);
  }, []);

  let getanalysis = async () => {
    let response = await fetch(`${process.env.REACT_APP_API_URL}/api/annotsv/`);
    let data = await response.json();

    let new_data = data;
    // console.log(data)
    console.log(new_data);
    setAnnotsv(new_data);
  };
  return (
    <div>
      <h2> Annotsv</h2>
    </div>
  );
};

export default AnnotSV;
