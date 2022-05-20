import Form from "react-bootstrap/Form";
import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
const WhoAmI = () => {
    let [applications, setApplications] = useState([]);

  useEffect(() => {
    getApplications();
  }, []);

  let getApplications = async () => {
    let response = await fetch(`${process.env.REACT_APP_API_URL}/api/users/`);
    let data = await response.json();

    let new_data = data.Response;
    // console.log(data)
    console.log(new_data);
    setApplications(new_data);
  };
    return (
        <div>
            <Form>
        <div className="row justify-content-center">
          <div className="col-10 justify-content-center">
            <div className="card">
              <div className="card-body">
                <h4 className="card-header d-flex justify-content-between align-items-center">
                  Id: {applications.Id}
                  <Link
                    to="/basic-ui/Basespace"
                    style={{ textDecoration: "none" }}
                  >
                    <button
                      type="button"
                      className="btn btn-sm"
                      style={{ backgroundColor: "#fec107" }}
                    >
                      Back{" "}
                    </button>
                  </Link>
                </h4>

                <div className="table-responsive">
                  <table className="table table-bordered  table-hover">
                    <tbody>
                      <tr>
                        <th>Name</th>
                        <td>{applications.Name}</td>
                      </tr>
                      <tr>
                        <th>Email</th>
                        <td>{applications.Email}</td>
                      </tr>
                     
                       <tr>
                        <th>DateCreated</th>
                        <td>
                            {applications.DateCreated}
                        </td>
                    </tr>
                    <tr>
                        <th>DateLastActive</th>
                        <td>
                            {applications.DateLastActive}
                        </td>
                    </tr>
                    <tr>
                        <th>Href</th>
                        <td>
                            {applications.Href}
                        </td>
                    </tr>
                    <tr>
                        <th>HrefProjects</th>
                        <td>
                            {applications.HrefProjects}
                        </td>
                    </tr>
                    <tr>
                        <th>HrefRuns</th>
                        <td>
                            {applications.HrefRuns}
                        </td>
                    </tr>
                    
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Form>
        </div>
    )
}

export default WhoAmI
