import React, { useEffect, useState } from "react";
import { Table } from "react-bootstrap";

import { ProgressBar } from "react-bootstrap";
const Vus = () => {
  const [VUS, setVUS] = useState([]);

  const [isLoading, setLoading] = useState(true);
  useEffect(() => {
    getVUS();
  }, []);

  let getVUS = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_vus/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();

    console.log(res);

    setVUS(res);

    setLoading(false);
  };
  return (
    <div>
      {/* <div className="page-header">
        <h3 className="page-title">
          {" "}
          Variants of Unknown Significance - Non Synonymous SNV
        </h3>
      </div> */}

      {/* <div className="row">
        <div className="col-lg-6 grid-margin stretch-card">
          <div className="card">
            <div className="card-body">
              <div className="table-responsive">
                <Table striped bordered hover responsive>
                  <thead style={{ backgroundColor: "#fec107" }}>
                    <tr>
                      <th>Gene</th>
                      <th>Variant CDS</th>
                      <th>Amino Acid Variant</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>TNFRSF14</td>
                      <td>T2245C</td>
                      <td>P262L</td>
                    </tr>

                    <tr>
                      <td>KIF1B</td>
                      <td>C785T</td>
                      <td>W749R</td>
                    </tr>
                    <tr>
                      <td>MST1</td>
                      <td>C881G</td>
                      <td>T294S</td>
                    </tr>
                    <tr>
                      <td>PTPRG</td>
                      <td>C1082T</td>
                      <td>T361M</td>
                    </tr>
                  </tbody>
                </Table>
              </div>
            </div>
          </div>
        </div>
        <div className="col-lg-6 grid-margin stretch-card">
          <div className="card">
            <div className="card-body">
              <div className="table-responsive">
                <Table striped bordered hover responsive>
                  <thead style={{ backgroundColor: "#fec107" }}>
                    <tr>
                      <th>Gene</th>
                      <th>Variant CDS</th>
                      <th>Amino Acid Variant</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>TNFRSF14</td>
                      <td>T2245C</td>
                      <td>P262L</td>
                    </tr>

                    <tr>
                      <td>KIF1B</td>
                      <td>C785T</td>
                      <td>W749R</td>
                    </tr>
                    <tr>
                      <td>MST1</td>
                      <td>C881G</td>
                      <td>T294S</td>
                    </tr>
                    <tr>
                      <td>PTPRG</td>
                      <td>C1082T</td>
                      <td>T361M</td>
                    </tr>
                  </tbody>
                </Table>
              </div>
            </div>
          </div>
        </div>
       </div> */}

      <div className="row">
        <div className="col-lg-12 grid-margin">
        <div className="card">
          <div className="card-body">
              <h4 className="card-title">
                Pharmacogenomic Biomarkers in Drug Labels - Targeted Therapies
              </h4>

              <div className="table-responsive">
                <table
                  className="table table-bordered text-wrap"
                  style={{ width: "auto" }}
                >
                  <thead style={{ backgroundColor: "#fec107" }}>
                    <tr>
                      <th>Drug </th>
                      <th> Biomarker</th>
                      <th> Variant status in patient </th>
                    </tr>
                  </thead>
                  <tbody>
                    {VUS.map((drug, index) => {
                      const condition = drug.STATUS === 'Positive';

                       let color =
                       drug.STATUS === "Negative"
                         ? ""
                         : drug.STATUS === "Positive"
                         ? "green"
                         : "";
                      return (
                        <tr key={index}>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                              color: condition ? "green" : ""
                            }}
                          >
                            {" "}
                            {drug.DRUG}
                          </td>
                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",
                              color: condition ? "green" : ""
                            }}
                          >
                            {" "}
                            {drug.BIOMARKER}
                          </td>

                          <td
                            style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",

                               color: color 
                            }}
                          >
                            {" "}
                            {drug.STATUS}
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

export default Vus;
