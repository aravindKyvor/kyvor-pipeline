import React, { useState, useEffect, Fragment } from "react";
import Table from "react-bootstrap/Table";
// import AddIcon from '@mui/icons-material/Add';
import { Link } from "react-router-dom";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { Spinner } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
toast.configure();
const Patientportal = (props) => {
  let [portal, setportal] = useState([]);
  let [physician_information, setphysician_information] = useState([]);
  let [reports, setreports] = useState([]);
  let [specimen, setspecimen] = useState([]);
  let [cancerType, setcancerType] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    // setInterval(function () {
    getportal();
    // }, 5000);
  }, []);

  let getportal = async () => {
    let response = await fetch(`${process.env.REACT_APP_API_URL}/api/portal/`);
    let data = await response.json();
    let res = data[0].Patient_information;
    let info = data[0].Physician_information;
    let reports_date = data[0].Report_Date;
    let specimens = data[0].Specimen;
    let cancertype = data[0].Cancer_Type;

    console.log(res);
    console.log(data);
    setportal(res);
    setphysician_information(info);
    setreports(reports_date);
    setspecimen(specimens);
    setcancerType(cancertype);
    setLoading(false);
  };
  return !isLoading ? (
    <div>
      <div className="row">
        <div className="col-12 grid-margin">
          <div className="card">
            <div className="card-body">
            <h4 className="card-header d-flex justify-content-between align-items-center">
                  Reports
                  <Link
                    to="/basic-ui/patient/form"
                    style={{ textDecoration: "none" }}
                  >
                    <i className='mdi mdi-plus'></i>
                  </Link>
                </h4>

                <hr />

              <Table responsive>
                <tbody>
                  <tr>
                    <th className="table-active">Patient Information</th>
                    <td>{portal}</td>
                  </tr>

                  <tr>
                    <th className="table-active">Physician Information</th>
                    <td>{physician_information}</td>
                  </tr>

                  <tr>
                    <th className="table-active">Reports</th>
                    <td>{reports}</td>
                  </tr>

                  <tr>
                    <th className="table-active">Specimen</th>
                    <td>{specimen}</td>
                  </tr>
                  <tr>
                    <th className="table-active">Cancertype</th>
                    <td>{cancerType}</td>
                  </tr>
                </tbody>
              </Table>
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

export default Patientportal;
