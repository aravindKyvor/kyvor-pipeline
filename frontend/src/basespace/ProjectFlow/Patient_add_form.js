import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { Form } from "react-bootstrap";
import { Link, useHistory } from "react-router-dom";
import { addPatientdata } from "../../actions/basespace";
import { toast } from "react-toastify";
import Modal from "react-bootstrap/Modal";

import "react-toastify/dist/ReactToastify.css";

toast.configure();
function validate(Patient_information) {
  const errors = [];

  if (Patient_information === "") {
    errors.push("please enter patient information Name");
  }
  return errors;
}
export class Patient_add_form extends Component {
  state = {
    Patient_information: "",
    Physician_information: "",
    Report_Date: "",
    Cancer_Type: "",
    Specimen: "",
  };
  static propTypes = {
    addPatientdata: PropTypes.func.isRequired,
  };

  // Input Change Handler
  changeHandler(event) {
    this.setState({
      [event.target.name]: event.target.value,
    });
  }

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    const {
      Patient_information,
      Physician_information,
      Report_Date,
      Cancer_Type,
      Specimen,
    } = this.state;
    const patientdata = {
      Patient_information,
      Physician_information,
      Report_Date,
      Cancer_Type,
      Specimen,
    };
    const errors = validate(Patient_information);
    if (errors.length > 0) {
      this.setState({ errors });
      return;
    } else if (errors.length === 0) {
      toast.success("Required Fields Are Entered Correctly");
    }

    this.props.addPatientdata(patientdata, errors);

    this.setState({
      Patient_information: "",
      Physician_information: "",
      Report_Date: "",
      Cancer_Type: "",
      Specimen: "",
    });
    this.props.history.push("/basic-ui/reports");
  };

  render() {
    const {
      errors,
      Patient_information,
      Physician_information,
      Report_Date,
      Cancer_Type,
      Specimen,
    } = this.state;

    return (
      <div>
        <div className="page-header">
          <h3 className="page-projectName"> Adding Patient Data Form </h3>
          <nav aria-label="breadcrumb">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                <a href="!#" onClick={(event) => event.preventDefault()}></a>
              </li>
            </ol>
          </nav>
        </div>

        <div className=" col-11 grid-margin stretch-card-1 ">
          <div className="card">
            <div className="card-body">
              <form className="forms-sample" onSubmit={this.onSubmit}>
                {errors &&
                  errors.map((error) => (
                    <div
                      class="alert alert-danger alert-dismissible"
                      role="alert"
                      key={error}
                    >
                      <strong>Error: {error}</strong>
                    </div>
                  ))}
                <Form.Group>
                  <label htmlFor="exampleInputUsername1">
                    Patient Information
                  </label>
                  <Form.Control
                    type="text"
                    id="exampleInputUsername1"
                    placeholder="Patient_information"
                    size="lg"
                    value={Patient_information}
                    name="Patient_information"
                    onChange={this.onChange}
                  />
                </Form.Group>
                <Form.Group>
                  <label htmlFor="exampleInputUsername1">
                    Physician Information
                  </label>
                  <Form.Control
                    type="text"
                    id="exampleInputUsername1"
                    placeholder="Physician_information"
                    size="lg"
                    value={Physician_information}
                    name="Physician_information"
                    onChange={this.onChange}
                    required
                  />
                </Form.Group>

                <Form.Group>
                  <label id="inputGroupFile04">Report Date</label>
                  <input
                    type="date"
                    className="form-control"
                    id="inputGroupFile04"
                    value={Report_Date}
                    name="Report_Date"
                    placeholder="Report_Date"
                    onChange={this.onChange}
                    required
                  />
                </Form.Group>

                <Form.Group>
                  <label id="inputGroupFile05">Cancer Type</label>
                  <input
                    id="inputGroupFile05"
                    type="text"
                    placeholder="Cancer_Type"
                    className="form-control"
                    value={Cancer_Type}
                    name="Cancer_Type"
                    onChange={this.onChange}
                    required
                  />
                </Form.Group>

                <Form.Group>
                  <label id="inputGroupFile05">Specimen</label>
                  <input
                    id="inputGroupFile05"
                    type="text"
                    placeholder="Specimen"
                    className="form-control"
                    value={Specimen}
                    name="Specimen"
                    onChange={this.onChange}
                    required
                  />
                </Form.Group>

                <div className="col text-center">
                  <button
                    type="submit"
                    className="btn  mr-2 btn-sm"
                    style={{ backgroundColor: "#fec107" }}
                  >
                    Submit
                  </button>
                </div>
              </form>
              <div className="border border-light p-3 mb-4">
                <div className="text-center">
                  <span>
                    <Link to="/basic-ui/reports">
                      <button className="btn btn-light btn-sm"> Cancel</button>
                    </Link>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default connect(null, { addPatientdata })(Patient_add_form);
