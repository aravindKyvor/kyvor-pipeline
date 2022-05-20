import React from "react";
import { useLocation, Link } from "react-router-dom";
import Form from "react-bootstrap/Form";
import { Card } from "react-bootstrap";
import "./style.css";
const ViewUserDetails = (_) => {
  const { state } = useLocation();

  return (
    <div>
      <Form>
        <div className="row justify-content-center">
          <div className="col-10 justify-content-center">
            <div className="card">
              <div className="card-body">
                <h4 className="card-header d-flex justify-content-between align-items-center">
                  Id: {state.applications.Id}
                  <Link
                    to="/basespace/applicationlist"
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
                        <th>Full Name</th>
                        <td>{state.applications.Name}</td>
                      </tr>
                      <tr>
                        <th>Href</th>
                        <td>{state.applications.Href}</td>
                      </tr>
                      <tr>
                        <th>HrefLogo</th>
                        <td>{state.applications.HrefLogo}</td>
                      </tr>
                      <tr>
                        <th>CompanyName</th>
                        <td>{state.applications.CompanyName}</td>
                      </tr>
                      <tr>
                        <th>HomepageUri</th>
                        <td>{state.applications.HomepageUri}</td>
                      </tr>
                      <tr>
                        <th>PublishStatus</th>
                        <td>{state.applications.PublishStatus}</td>
                      </tr>
                      <tr>
                        <th>IsBillingActivated</th>
                        <td>
                          {state.applications.IsBillingActivated
                            ? "true"
                            : "false"}
                        </td>
                      </tr>
                      {/* <tr>
                        <th>Features</th>
                        <td>
                            {state.applications.Features}
                        </td>
                    </tr> */}
                      <tr>
                        <th>AppFamilySlug</th>
                        <td>{state.applications.AppFamilySlug}</td>
                      </tr>
                      <tr>
                        <th>AppVersionSlug</th>
                        <td>{state.applications.AppVersionSlug}</td>
                      </tr>
                      <tr>
                        <th>Category</th>
                        <td>{state.applications.Category}</td>
                      </tr>
                      <tr>
                        <th>DateCreated</th>
                        <td>{state.applications.DateCreated}</td>
                      </tr>
                      <tr>
                        <th>DatePublished</th>
                        <td>{state.applications.DatePublished}</td>
                      </tr>
                      {/* <tr>
                        <th>Classification</th>
                        <td>
                            {state.applications.Classification}
                        </td>
                    </tr>
                    */}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Form>
    </div>
  );
};

export default ViewUserDetails;
