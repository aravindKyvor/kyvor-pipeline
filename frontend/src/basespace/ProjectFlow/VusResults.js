

import { Spinner } from "react-bootstrap";


import React from "react";

import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";
import AddIcon from "@material-ui/icons/Add";
import DeleteIcon from "@material-ui/icons/Delete";
import EditIcon from "@material-ui/icons/Edit";
import { ToastContainer, toast } from "react-toastify";
class VusResults extends React.Component {
  constructor() {
    super();
    this.state = {
      data: [],
      data2: [],
            isLoading: false,
    };
  }

  fetchSNVData() {
    fetch("http://localhost:8000/api/snv_database/")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          data: data,
          isLoading: true,
        });
      });
  }

  fetchINDELData() {
    fetch("http://localhost:8000/api/indel_database/")
      .then((response) => response.json())
      .then((data2) => {
        this.setState({
          data2: data2,
          isLoading: true,
        });
      });
  }

  componentDidMount() {
    this.fetchSNVData();
    this.fetchINDELData();
  }

  deleteData(id) {
    if (window.confirm("Are you sure want to delete the SNV datas")) {
      fetch("http://localhost:8000/api/snv_database/" + id + "/", {
        method: "DELETE",
        body: JSON.stringify(this.state),
      })
        .then((response) => response)
        .then((data) => {
          if (data) {
            this.fetchSNVData();
          }
        })
        .catch((err) => {
          console.log("Error", err);
          if (err) {
            toast.error("Clinical data was not deleted", {
              position: "top-right",
              autoClose: 2000,
            });
          }
        });
    }
  }

  deleteINDELData(id) {
    // if (window.confirm("Are you sure want to delete the SNV datas")) {
      fetch("http://localhost:8000/api/indel_database/" + id + "/", {
        method: "DELETE",
        body: JSON.stringify(this.state),
      })
        .then((response) => response)
        .then((data2) => {
          if (data2) {
            this.fetchINDELData();
          }
        })
        .catch((err) => {
          console.log("Error", err);
          if (err) {
            toast.error("Clinical data was not deleted", {
              position: "top-right",
              autoClose: 2000,
            });
          }
        });
    // }
  }

  render() {
    const { isLoading } = this.state;
    const SNVData = this.state.data;
    const rows = SNVData.map((application) => (
        <tr key={application.id}>
          <td>{application.GENE}</td>
          <td>{application.CDS}</td>
          <td>{application.AMINO_ACID_CHANGE}</td>
          <td >
            <DeleteIcon onClick={() => this.deleteData(application.id)} />


          </td>
        </tr>

    ));
    const INdelData = this.state.data2;
    const rows2 = INdelData.map((application) => (
        <tr key={application.id}>
          <td>{application.GENE}</td>
          <td>{application.CDS}</td>
          <td>{application.AMINO_ACID_CHANGE}</td>
          <td >
            <DeleteIcon onClick={() => this.deleteINDELData(application.id)} />


          </td>
        </tr>

    ));




    return (

      <React.Fragment>

        {

          !isLoading ? (
            <div className="container" style={{ textAlign: "center" }}>
              <Spinner animation="border" role="status">
                <span className="sr-only">Loading...</span>
              </Spinner>
            </div>
          ) : (
            <div>

<div className="row">
        <div className="col-lg-6 grid-margin ">
          <div className="card">
            <div className="card-body">
              <h4 className="card-header d-flex justify-content-between align-items-center">
                Variants of Unknown Significance - Non Synonymous SNV
              </h4>
              <br></br>
              <div className="table-responsive">
              <table className="table table-bordered">
                  <thead style={{ backgroundColor: "#fec107" }}>
                   
                    <tr>
                      <th>Gene</th>
                      <th>Variant CDS</th>
                      <th>Amino Acid Variant</th>
                      <th>Actions</th>
                    </tr>
                  
                  </thead>
                  <tbody>
                    {rows}
                  </tbody>
                  </table >
              </div>
            </div>
          </div>
        </div>
        <div className="col-lg-6 grid-margin ">
          <div className="card">
            <div className="card-body">
              <h4 className="card-header d-flex justify-content-between align-items-center">
                Variants of Unknown Significance - Short InDels
              </h4>
              <br></br>
              <div className="table-responsive">
              <table className="table table-bordered">
                  <thead style={{ backgroundColor: "#fec107" }}>
                  
                    <tr>
                      <th>Gene</th>
                      <th>Variant CDS</th>
                      <th>Amino Acid Variant</th>
                      <th>Actions</th>
                    </tr>
                   
                  </thead>
                  <tbody>
                  {rows2}
                  </tbody>
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

export default VusResults;