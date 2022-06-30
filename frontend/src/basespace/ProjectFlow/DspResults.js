import { ListItem } from "@material-ui/core";
import React, { useState, useEffect, Fragment } from "react";
import { Table } from "react-bootstrap";
import { Spinner } from "react-bootstrap";

import { ProgressBar } from "react-bootstrap";

const DspResults = () => {
  let [DSP, setDSP] = useState([]);
  const [isLoading, setLoading] = useState(true);
  

  useEffect(() => {
   
      getDSP();
  
  }, []);
  let getDSP = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/dsp_results/`
    );
    let data = await response.json();

    console.log(data);
    setDSP(data);
    setLoading(false);
  };

  return !isLoading ? (
    <div>
      <div className="row">
        <div className="col-lg-12 grid-margin">
          <div className="card">
            <div className="card-body">
              <h4 className="card-title">
                DSP Results
              </h4>

              <div className="table-responsive">
                <table
                  className="table table-borDSPred text-wrap"
                  style={{ width: "auto" }}
                >
                  <thead style={{ backgroundColor: "#fec107" }}>
                    <tr>
                      <th>Gene.refGene </th>
                      <th> AAChange</th>
                      <th>  AAChange Exon </th>
                      <th>CLNSIG </th>
                      <th> AF_VAF</th>
                      <th> Variant </th>
                      <th>  Psuedovariant </th>

                      <th> Therapy</th>
                      <th> Cancer Type</th>
                      <th>Evidence Statement </th>
                      <th> Significance</th>
                      <th> Levels Of Evidences </th>
                      <th>  Refrences </th>
                    </tr>
                  </thead>
                  <tbody>
                    {DSP.map((item, inDSPx) => {
                      return (
                        <tr key={inDSPx}>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.Gene}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.AAChange}
                          </td>

                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.AAChange_Exon}
                          </td>

                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.CLNSIG}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.AF_VAF}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.Variant}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.PSEUDOVARIANT}
                          </td>





                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.THERAPY}
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
                            {item.SIGNIFICANCE}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.LEVELS_OF_EVIDENCE}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                            }}
                          >
                            {" "}
                            {item.REFERENCES}
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
  ) : (
    <div className="container" style={{ textAlign: "center" }}>
      <Spinner animation="border" role="status">
        <span className="sr-only">Loading...</span>
      </Spinner>
    </div>
  );
};

export default DspResults;
