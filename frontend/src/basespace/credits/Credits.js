import Form from "react-bootstrap/Form";
import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
import { Spinner } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
const WhoAmI = () => {
  let [applications, setApplications] = useState([]);
  const [isLoading, setLoading] = useState(true)

  useEffect(() => {
    getApplications();
  }, []);

  let getApplications = async () => {
    let response = await fetch(`${process.env.REACT_APP_API_URL}/api/credits/`);
    let data = await response.json();

    let new_data = data.Wallet;
    // console.log(data)
    console.log(new_data);
    setApplications(new_data);
    setLoading(false)

  };
  return !isLoading?(
    <div>
      <div style={{ maxWidth: "90%", margin: "5vh auto" }}>
        <div className="page-header">
          <h3 className="page-title">
            <span className="page-title-icon bg-gradient-primary text-white mr-2">
              <i
                className="mdi mdi-credit-card "
                style={{ color: "black" }}
              ></i>
            </span>{" "}
            Credits Remaning{" "}
          </h3>
          <br />
        </div>
      </div>

      <Form>
        <div className="row justify-content-center">
          <div className="col-8 justify-content-center">
            <div className="card">
              <div className="card-body">
                <h4 className="card-header d-flex justify-content-between align-items-center">
                  Credits
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
                        <th>ICreditBalance</th>
                        <td>{applications.ICreditBalance}</td>
                      </tr>
                      <tr>
                        <th>ICreditUsage</th>
                        <td>{applications.ICreditUsage}</td>
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
  ):(
    <div className='container' style={{textAlign: 'center'}}>
    <Spinner animation="border" role="status">
            <span className="sr-only">Loading...</span>
          </Spinner>
    </div>
      )
      
};

export default WhoAmI;
