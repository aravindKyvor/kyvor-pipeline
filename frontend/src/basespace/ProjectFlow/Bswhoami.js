import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
import { Spinner } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
const BsWhoAmi = (props) => {
  let [applications, setApplications] = useState([]);
 

  useEffect(() => {
    getApplications();
  }, []);

  let getApplications = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_whoami/`
    );
    let data = await response.json();
    
   

    console.log(data);
    setApplications(data);
   
  };
  return  (
   <div></div>
  )};

export default BsWhoAmi;
