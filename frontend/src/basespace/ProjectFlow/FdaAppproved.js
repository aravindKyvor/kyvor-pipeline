import React, { useState, useEffect } from "react";
import { Table } from "react-bootstrap";
const FdaAppproved = () => {

  let [FDA, setFDA] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    setInterval(function () {
      getFDA();
    }, 1000);
  }, []);

  let getFDA = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_fda/`
    );
    let data = await response.json();

    console.log(data);
    setFDA(data);
    setLoading(false);
  };
  return (
    <div>
      <div className="row">
        <div className="col-12 grid-margin">
          <div className="card">
            <div className="card-body">
              <h4 className="card-title">
                FDA Approved Recommendations - Patient Cancer type
              </h4>
              <div className="table-responsive">
              <table className="table table-bordered text-wrap" style={{width:'auto'}}  >
                <thead style={{ backgroundColor: "#fec107" }}>
                  <tr>
                    <th style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>Biomarker</th>
                    <th style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>Therapy</th>
                    <th style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>
                      {" "}
                      Variant Status in patient DNA (Variant Allele Frequency)
                    </th>
                    <th style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>Reference</th>
                  </tr>
                </thead>
                <tbody >
                  No FDA approved biomarkers identified in this patient
                </tbody>
              </table>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="row">
        <div className="col-12 grid-margin">
          <div className="card">
            <div className="card-body">
              <h4 className="card-title">
                FDA Approved Recommendations - Other Cancer type{" "}
              </h4>
              <div className="table-responsive">
              <table className="table table-bordered text-wrap" style={{width:'auto'}}  >
              <thead style={{ backgroundColor: "#fec107" }}>
            <tr>
              <th  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>
                <strong>BioMarker</strong>
              </th>
              <th  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>
                <strong>THERAPY</strong>
              </th>
              <th  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>
                <strong>Status</strong>
              </th>
              <th  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>
                <strong>AF_VAF</strong>
              </th>
              <th  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>
                <strong>EVIDENCE_STATEMENT_1</strong>
              </th>
             
             
            </tr>
          </thead>
                <tbody>
            {FDA.map((application, index) => {
              // let color =
              //   application.bs_analysis_status === "Initializing"
              //     ? "red"
              //     : application.bs_analysis_status === "Running"
              //     ? "orange"
              //     : "green";
              return (
                <tr key={index}>
                  <td  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}> {application.BIOMARKER}</td>
                  <td> {application.THERAPY}</td>

                  <td  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}> {application.Status}</td>
                  <td  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}> {application.AF_VAF}</td>
                  <td  style={{whiteSpace: 'pre-wrap', overflowWrap: 'break-word'}}>
                    {" "}
                    {application.EVIDENCE_STATEMENT_1	}
                  </td>
                </tr>
              );
            })}
          </tbody>
              </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FdaAppproved;
