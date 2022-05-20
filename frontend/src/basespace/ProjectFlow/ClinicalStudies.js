import React, { useState, useEffect, Fragment } from "react";
import { Table } from "react-bootstrap";
import { Spinner } from "react-bootstrap";

import { ProgressBar } from "react-bootstrap";

const ClinicalStudies = () => {
  let [studies, setstudies] = useState([]);
  const [isLoading, setLoading] = useState(true);
  // eslint-disable-next-line no-use-before-define

  useEffect(() => {
    setInterval(function () {
      getstudies();
    }, 2000);
  }, []);
  let getstudies = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_clinicalreport/`
    );
    let data = await response.json();

    console.log(data);
    setstudies(data);
    setLoading(false);
  };

  return !isLoading ? (
    <div>
      <div className="col-lg-12 grid-margin">
        <div className="card">
          <div className="card-body">
            <h4 className="card-title">Clinical & Case Studies </h4>

            <div className="table-responsive">
              <table
                className="table table-bordered text-wrap"
                style={{ width: "auto" }}
              >
                <tr>
                  <th style={{ backgroundColor: "#fec107" }}>Biomarker</th>

                  <th style={{ backgroundColor: "#fec107" }}>Therapy</th>
                  <th
                    style={{
                      backgroundColor: "#fec107",
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    {" "}
                    Variant Status in patient DNA (Variant Allele Frequency)
                  </th>
                  <th style={{ backgroundColor: "#fec107" }}>Reference</th>
                </tr>
                {studies.map((application, index) => {
                  return (
                    <Fragment>
                      <tr key={index}>
                        <td rowspan="2">{application.BioMarker}</td>

                      
                         
                        <td
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          {application.intervention}
                        </td>
                        <td
                          style={{
                           
                            textAlign: "left",                          }}
                        >
                          {application.Status}
                        </td>
                        <td
                          style={{
                            // whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                            textAlign: "left", 
                          }}
                        >
                          <a href={application.url} target="_blank" rel="noopener noreferrer"
                          className="btn btn-link"
                          style={{ textDecoration: "none" }}
                          > {application.Reference}</a>
                        </td>
                      </tr>

                      <tr>
                        <td
                          colspan="4"
                          style={{
                            whiteSpace: "pre-wrap",
                            textAlign: "center",
                          }}
                        >
                          {application.official_title}
                        </td>
                      </tr>
                    </Fragment>
                  );
                })}
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  ) : (
    //     </div>
    //   </div>
    // </div>
    <div className="container" style={{ textAlign: "center" }}>
      <Spinner animation="border" role="status">
        <span className="sr-only">Loading...</span>
      </Spinner>
    </div>
  );
};

export default ClinicalStudies;
