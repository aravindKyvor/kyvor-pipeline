import React, { useState, useEffect } from "react";

import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { Spinner } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
toast.configure();
const ApplicationList = (props) => {
  let [analysis, setanalysis] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    setInterval(function () {
      getanalysis();
    }, 5000);
  }, []);

  let getanalysis = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/analysis_latest/`
    );
    let data = await response.json();

    console.log(data);
    setanalysis(data);
    setLoading(false);
  };
  return !isLoading ? (
    <div>
      <div className="page-header">
        <h3 className="page-title">Analysis Lists </h3>
      </div>
      <br />

      <div className="table-responsive">
        <table className="table table-bordered  table-hover">
          <thead style={{ backgroundColor: "#fec107" }}>
            <tr>
              <th>
                <strong>Analysis Description</strong>
              </th>
              <th>
                <strong>Analysis Ref id</strong>
              </th>
              <th>
                <strong>Analysis Type</strong>
              </th>
              <th>
                <strong>Bs_Analysis_Id</strong>
              </th>
              <th>
                <strong>Bs_Analysis Status</strong>
              </th>
            </tr>
          </thead>
          <tbody>
            {analysis.map((application, index) => {
              let color =
                application.bs_analysis_status === "Initializing"
                  ? "red"
                  : application.bs_analysis_status === "Running"
                  ? "orange"
                  : "green";
              return (
                <tr key={index}>
                  <td> {application.analysis_description}</td>
                  <td> {application.analysis_ref_id}</td>

                  <td> {application.analysis_type}</td>
                  <td> {application.bs_analysis_id}</td>
                  <td style={{ color: color }}>
                    {" "}
                    {application.bs_analysis_status}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
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

export default ApplicationList;



