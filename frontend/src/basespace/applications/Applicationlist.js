import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
import { Spinner } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
const ApplicationList = (props) => {
  let [applications, setApplications] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    getApplications();
  }, []);

  let getApplications = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/applications/`
    );
    let data = await response.json();
    console.log(data.Response.Items);
    let new_data = data.Response.Items;
    // console.log(data)
    console.log(new_data);
    setApplications(new_data);
    setLoading(false);
  };
  return !isLoading ? (
    <div>
      <div className="page-header">
        <h3 className="page-title">Application Lists </h3>
      </div>
      <br />
      <div className="table-responsive">
        <table className="table table-bordered  table-hover">
          <thead style={{ backgroundColor: "#fec107" }}>
            <tr>
              <th>
                <strong>ApplicationId</strong>
              </th>
              <th>
                <strong>ApplicationName</strong>
              </th>
              <th>
                <strong>CompanyName</strong>
              </th>
              <th>
                <strong>ApplicationHref</strong>
              </th>
            </tr>
          </thead>
          <tbody>
            {applications.map((application, index) => {
              return (
                <tr key={index}>
                  <td>
                    {" "}
                    <Link
                      to={{
                        pathname: `/view/${application.Id}`,
                        state: { applications: application },
                      }}
                      className="btn btn-link"
                      style={{ textDecoration: "none" }}
                    >
                      {application.Id}
                    </Link>
                  </td>
                  <td> {application.Name}</td>
                  <td> {application.CompanyName}</td>
                  <td> {application.Href}</td>
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
