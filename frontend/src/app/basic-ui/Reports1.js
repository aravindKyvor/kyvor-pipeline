import React from "react";

const Reports1 = () => {
  return (
    <div>
      <div className="row">
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <div className="card-body">
              <h4 className="font-weight-normal mb-3 text-center">
                Patient ID{" "}
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
              <h4 className="font-weight-normal mb-3 text-center">
                Patient Name
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
              <h4 className="font-weight-normal mb-3 text-center">
                Cancer Type
              </h4>
            </div>
          </div>
        </div>
      </div>
      <div className="col-12">
        <p
          className="btn btn-secondary btn-lg btn-block "
          style={{ color: "black" }}
        >
          Reports/Patient ID
        </p>
      </div>

      <div className="row">
        <div className="col-md-4 stretch-card grid-margin">
          <div
            className="card  card-img-holder text-black"
            style={{ backgroundColor: "#fec107" }}
          >
            <div className="card-body">
              <h4 className="font-weight-normal mb-3 text-center">
                Annotated Files{" "}
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
              <h4 className="font-weight-normal mb-3 text-center">
                BioSamples
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
              <h4 className="font-weight-normal mb-3 text-center">
                Clinical Trials
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
            <div className="card-body">
              <h4 className="font-weight-normal mb-3 text-center">
                DE Outputs{" "}
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
              <h4 className="font-weight-normal mb-3 text-center">
                DSP Outputs
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
              <h4 className="font-weight-normal mb-3 text-center">MSI</h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Reports1;
