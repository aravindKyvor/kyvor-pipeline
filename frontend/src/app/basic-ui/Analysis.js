import React from "react";

import { Link } from "react-router-dom";
const Analysis = () => {
  return (
    <div>
      <div className="page-header">
        <h3 className="page-title">
          <span className="page-title-icon bg-gradient-primary text-white mr-2">
            <i className="mdi mdi-file-find " style={{ color: "black" }}></i>
          </span>{" "}
          Analysis{" "}
        </h3>
        <br />
      </div>
      <div className="row">
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <Link
              to="/analysis/projectform"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                {/* <img src="" className="card-img-absolute" alt="circle" /> */}
                <h4 className="font-weight-normal mb-3 text-center">
                  TO Pipeline{" "}
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
            <Link
              to="/analysis/tnprojectform"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                {/* <img src="" className="card-img-absolute" alt="circle" /> */}
                <h4 className="font-weight-normal mb-3 text-center">
                  TN Pipeline{" "}
                </h4>
              </div>
            </Link>
          </div>
        </div>
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
      </div>
      <div className="row">
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <Link
              to="/basic-ui/DSPcuration"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                {/* <img src="" className="card-img-absolute" alt="circle" /> */}
                <h4 className="font-weight-normal mb-3 text-center">
                  DSP Curation{" "}
                </h4>
              </div>
            </Link>
          </div>
        </div>
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <Link
              to="/basic-ui/DEcuration"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                {/* <img src="" className="card-img-absolute" alt="circle" /> */}
                <h4 className="font-weight-normal mb-3 text-center">
                  DE Curation{" "}
                </h4>
              </div>
            </Link>
          </div>
        </div>
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <div className="card-body">
              {/* <img src="" className="card-img-absolute" alt="circle" /> */}
              <h4 className="font-weight-normal mb-3 text-center">
                DGP Curation{" "}
              </h4>
            </div>
          </div>
        </div>
      </div>
      <div className="row">
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <Link
              to="/basic-ui/AnnovarRun"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                {/* <img src="" className="card-img-absolute" alt="circle" /> */}
                <h4 className="font-weight-normal mb-3 text-center">
                  Annovar{" "}
                </h4>
              </div>
            </Link>
          </div>
        </div>
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <Link
              to="/basic-ui/AnnotSV"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                {/* <img src="" className="card-img-absolute" alt="circle" /> */}
                <h4 className="font-weight-normal mb-3 text-center">
                  AnnotSV{" "}
                </h4>
              </div>
            </Link>
          </div>
        </div>
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <Link
              to="/basic-ui/Msisensor"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                {/* <img src="" className="card-img-absolute" alt="circle" /> */}
                <h4 className="font-weight-normal mb-3 text-center">
                  MSI Sensor{" "}
                </h4>
              </div>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Analysis;
