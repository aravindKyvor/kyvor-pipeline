import React, { useState } from 'react';
// import { useHistory } from 'react-router-dom';

import { Link } from "react-router-dom";
// import axios, { post } from 'axios';
import logo2 from "../../assets/images/dashboard/circle.svg";
import logo3 from "../../assets/images/dashboard/circle.svg";
// import { Form } from "react-bootstrap";
import { toast } from "react-toastify";
// import {Redirect} from 'react-router-dom';

import "react-toastify/dist/ReactToastify.css";

toast.configure();

const Dashboard = () => {
  
<div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <Link
              to="/basic-ui/clinicalTrails"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                {/* <img src="" className="card-img-absolute" alt="circle" /> */}
                <h4 className="font-weight-normal mb-3 text-center">
                  Clinical Trails{" "}
                </h4>
              </div>
            </Link>
          </div>
        </div>
  



  
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">
            <span className="page-title-icon bg-gradient-primary text-white mr-2">
              <i className="mdi mdi-home"></i>
            </span>{" "}
            Dashboard{" "}
          </h3>
          <nav aria-label="breadcrumb">
            <ul className="breadcrumb">
              <li className="breadcrumb-data active" aria-current="page">
                <span></span>Overview{" "}
                <i className="mdi mdi-alert-circle-outline icon-sm text-primary align-middle"></i>
              </li>
            </ul>
          </nav>
        </div>
        <div className="row">
          <div className="col-md-4 stretch-card grid-margin">
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Link
                to="/basic-ui/analysisform"
                style={{ color: "black", textDecoration: "none" }}
              >
                <div className="card-body">
                  <img src={logo3} className="card-img-absolute" alt="circle" />
                  <h4 className="font-weight-normal mb-3 text-center">
                    Analysis{" "}
                    <i className="mdi mdi-file-find mdi-36px float-right"></i>
                  </h4>
                </div>
              </Link>
            </div>
          </div>
          <div className="col-md-4 stretch-card grid-margin">
            <div
              className="card card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <div className="card-body">
                <img src={logo2} className="card-img-absolute" alt="circle" />
                <h4 className="font-weight-normal mb-3 text-center">
                  Link To Reports{" "}
                  <i className="mdi mdi-information mdi-36px float-right"></i>
                </h4>
              </div>
            </div>
          </div>
          <div className="col-md-4 stretch-card grid-margin">
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <div className="card-body">
                <img src={logo3} className="card-img-absolute" alt="circle" />
                <h4 className="font-weight-normal mb-3 text-center">
                  Link To Patient Portal{" "}
                  <i className="mdi mdi-seat-individual-suite mdi-36px float-right"></i>
                </h4>
              </div>
            </div>
          </div>
        </div>

     
      </div> 
    );
  
              }

export default Dashboard;