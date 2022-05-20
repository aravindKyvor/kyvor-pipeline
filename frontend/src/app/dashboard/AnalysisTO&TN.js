import React from "react";

import { Link } from "react-router-dom";
const AnalysisForm = () => {
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
        <div className="col-md-5 stretch-card grid-margin">
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
        <div className="col-md-5 stretch-card grid-margin">
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
        
      </div>
     
     
    </div>
  );
};

export default AnalysisForm;
