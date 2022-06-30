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

  let [specimen, setspecimen] = useState([]);
  let [cancerType, setcancerType] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    getportal();
  }, []);

  let getportal = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/patient_ids/`
    );
    let data = await response.json();
    let res = data[0].Patient_Information;
    let info = data[0].Physician_information;

    let specimens = data[0].Final_results_colum;
    let cancertype = data[0].patient_cancer_type;

    // console.log(res);
    console.log(data);

    setphysician_information(info);
    setportal(res);
    setspecimen(specimens);
    setcancerType(cancertype);
    setLoading(false);
  };
  return (
    <div>
      <div className="row">
        <div className="col-12 grid-margin">
          <div className="card">
            <div className="card-body">


              
              <h4 className="card-header d-flex justify-content-between align-items-center">
                Reports
              </h4>

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
                    <th className="table-active">Specimen</th>
                    <td> {specimen}</td>
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
  );
};

export default Patientportal;
