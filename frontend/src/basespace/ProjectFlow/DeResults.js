import { ListItem } from "@material-ui/core";
import React, { useState, useEffect, Fragment } from "react";
import { Table } from "react-bootstrap";
import { Spinner } from "react-bootstrap";

import { ProgressBar } from "react-bootstrap";

const DeResults = () => {
  let [DE, setDE] = useState([]);
  const [isLoading, setLoading] = useState(true);
  // eslint-disable-next-line no-use-before-define

  useEffect(() => {
   
      getDE();
   
  }, []);
  let getDE = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/de_results/`
    );
    let data = await response.json();

    console.log(data);
    setDE(data);
    setLoading(false);
  };

  return !isLoading ?  (
    <div>
      <div className="row">
        <div className="col-lg-12 grid-margin">
          <div className="card">
            <div className="card-body">
              <h4 className="card-title">
                DE Results
              </h4>

              <div className="table-responsive">
                <table
                  className="table table-bordered text-wrap"
                  style={{ width: "auto" }}
                >
                  <thead style={{ backgroundColor: "#fec107" }}>
                    <tr>
                      <th>Biomarker </th>
                      <th> CN</th>
                      <th> Cancer Type </th>
                      <th>Evidence Statement </th>
                      <th> Reference</th>
                      <th> Therapy </th>
                      <th> Variant status in patient </th>
                    </tr>
                  </thead>
                  <tbody>
                    {DE.map((item, index) => {
                      return (
                        <tr key={index}>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.Biomarker}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.CN}
                          </td>

                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.Cancer_Type}
                          </td>

                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.EVIDENCE_STATEMENT}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.Reference}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.Therapy}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.Variant_status_in_patient}
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
  ):(
    <div className="container" style={{ textAlign: "center" }}>
      <Spinner animation="border" role="status">
        <span className="sr-only">Loading...</span>
      </Spinner>
    </div>
  )
};

export default DeResults;
