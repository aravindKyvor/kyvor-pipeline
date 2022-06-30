import { Spinner } from "react-bootstrap";


import React from "react";
import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";
import AddIcon from "@material-ui/icons/Add";
import DeleteIcon from "@material-ui/icons/Delete";
import EditIcon from "@material-ui/icons/Edit";
import { ToastContainer, toast } from "react-toastify";
class FdaAppproved extends React.Component {
  constructor() {
    super();
    this.state = {
      data: [],
      isLoading: false,
    };
  }

  fetchData() {
    fetch("http://localhost:8000/api/fda/")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          data: data,
          isLoading: true,
        },() => {
          console.log(this.state.data)});
      });
  }

  componentDidMount() {
    this.fetchData();
  }

  deleteData(id) {
    if (window.confirm("Are you sure want to delete the FDA datas")) {
      fetch("http://localhost:8000/api/fda/" + id + "/", {
        method: "DELETE",
        body: JSON.stringify(this.state),
      })
        .then((response) => response)
        .then((data) => {
          if (data) {
            this.fetchData();
          }
        })
        .catch((err) => {
          console.log("Error", err);
          if (err) {
            toast.error("FDA data was not deleted", {
              position: "top-right",
              autoClose: 2000,
            });
          }
        });
    }
  }

  render() {
    const { isLoading} = this.state;
    const fdaData = this.state.data;
    const rows = fdaData.map((item) => (
      <tr key={item.id}>
        <td style={{ whiteSpace: "pre-wrap", overflowWrap: "break-word" }}>
          {" "}
          {item.BIOMARKER}
        </td>
        <td> {item.THERAPY}</td>

        <td style={{ whiteSpace: "pre-wrap", overflowWrap: "break-word" }}>
          {" "}
          {item.Status}
        </td>
        <td style={{ whiteSpace: "pre-wrap", overflowWrap: "break-word" }}>
          {" "}
          {item.AF_VAF}
        </td>
        <td style={{ whiteSpace: "pre-wrap", overflowWrap: "break-word" }}>
          {" "}
          {item.EVIDENCE_STATEMENT_1}
        </td>

        <td>
          <DeleteIcon onClick={() => this.deleteData(item.id)} />
        </td>
      </tr>
    ));
    return  (
    
       <React.Fragment>

        {

          !isLoading ?(
            <div className="container" style={{ textAlign: "center" }}>
            <Spinner animation="border" role="status">
              <span className="sr-only">Loading...</span>
            </Spinner>
          </div>
          ):(
            <div>
<div className="row">
          <div className="col-12 grid-margin">
            <div className="card">
              <div className="card-body">
                <h4 className="card-title">
                  {" "}
                  FDA Approved Recommendations - Patient Cancer type
                </h4>
                <div className="table-responsive">
                  <table
                    className="table table-bordered text-wrap"
                    style={{ width: "auto" }}
                  >
                    {" "}
                    <thead style={{ backgroundColor: "#fec107" }}>
                      <tr>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          Biomarker
                        </th>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          Therapy
                        </th>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          {" "}
                          Variant Status in patient DNA (Variant Allele
                          Frequency)
                        </th>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          Reference
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      No FDA approved biomarkers identified in this patient
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="row">
          <div className="col-12 grid-margin">
            <div className="card">
              <div className="card-body">
                <h4 className="card-header d-flex justify-content-between align-items-center">
                  FDA Approved Recommendations - Patient Cancer type
                </h4>

                <hr />

                <div className="table-responsive">
                  <table className="table table-bordered  table-hover">
                    <thead style={{ backgroundColor: "#fec107" }}>
                      <tr>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          <strong>BioMarker</strong>
                        </th>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          <strong>THERAPY</strong>
                        </th>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          <strong>Status</strong>
                        </th>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          <strong>AF_VAF</strong>
                        </th>
                        <th
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          <strong>EVIDENCE_STATEMENT_1</strong>
                        </th>
                        <th
                          colSpan="1"
                          style={{
                            whiteSpace: "pre-wrap",
                            overflowWrap: "break-word",
                          }}
                        >
                          {" "}
                          <strong>Actions</strong>{" "}
                        </th>
                      </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
        </div>
          )
        }
        
        </React.Fragment>
    )

  
  }

}

export default FdaAppproved;
