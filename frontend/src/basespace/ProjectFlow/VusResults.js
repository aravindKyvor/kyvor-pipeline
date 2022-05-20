import React, { useEffect, useState } from "react";
import { Table } from "react-bootstrap";

import { ProgressBar } from "react-bootstrap";
const VusResults = () => {
  const [Indel, setIndel] = useState([]);
  const [Snv, setSnv] = useState([]);
  const [isLoading, setLoading] = useState(true);
  useEffect(() => {
    setInterval(function () {
      getVusResults();
    }, 1000);
  }, []);

  let getVusResults = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/vus_results/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();
    let snv_file = res.snv;
    let indel_file = res.indel;
    console.log(snv_file);
    console.log(indel_file);
    setSnv(snv_file);
    setIndel(indel_file);

    setLoading(false);
  };
  return (
    <div>
      <div className="page-header">
        <h3 className="page-title">
          {" "}
          Variants of Unknown Significance - Non Synonymous SNV
        </h3>
      </div>

      <div className="row">
        <div className="col-lg-6 grid-margin ">
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
                    {Snv.map((item,index) => {
                        return(
                            <tr key={index}>
                            <td>{item.GENE}</td>
                            <td>{item.CDS}</td>
                            <td>{item.AMINO_ACID_CHANGE}</td>
                          </tr>
                        )
                     
                    })}
                  </tbody>
                </Table>
              </div>
            </div>
          </div>
        </div>
        <div className="col-lg-6 grid-margin ">
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
                    {Indel.map((item,index) => {
                        return(
                            <tr key={index}>
                            <td>{item.GENE}</td>
                            <td>{item.CDS}</td>
                            <td>{item.AMINO_ACID_CHANGE}</td>
                          </tr>
                        )
                     
                    })}
                  </tbody>
                </Table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default VusResults;
