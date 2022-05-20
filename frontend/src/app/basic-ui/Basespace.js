import React from "react";
import { Link } from "react-router-dom";
const Basespace = () => {
  return (
    <div>
      <div className="page-header">
        <h3 className="page-title">
          <span className="page-title-icon bg-gradient-primary text-white mr-2">
            <i
              className="mdi mdi-human-male-female "
              style={{ color: "black" }}
            ></i>
          </span>{" "}
          Basespace{" "}
        </h3>
        <br />
      </div>

      <div className="row">
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <Link
              to="/basespace/projects/list"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                <h4 className="font-weight-normal mb-3 text-center">
                  Projects{" "}
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
              to="/basespace/users/whoami"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                <h4 className="font-weight-normal mb-3 text-center">WhoAmI</h4>
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
              to="/basespace/biosample"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                <h4 className="font-weight-normal mb-3 text-center">
                  Biosamples
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
            {/* /basespace/analysis */}
            <Link
              to="/basespace/analysis"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                <h4 className="font-weight-normal mb-3 text-center">
                  Analysis{" "}
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
              to="/basespace/applicationlist"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                <h4 className="font-weight-normal mb-3 text-center">
                  Applications
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
              to="/basespace/credits"
              style={{ color: "black", textDecoration: "none" }}
            >
              <div className="card-body">
                <h4 className="font-weight-normal mb-3 text-center">
                  Credits Remaining
                </h4>
              </div>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Basespace;
