
import { Spinner } from "react-bootstrap";


import React from "react";

import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";
import AddIcon from "@material-ui/icons/Add";
import DeleteIcon from "@material-ui/icons/Delete";
import EditIcon from "@material-ui/icons/Edit";
import { ToastContainer, toast } from "react-toastify";
class FinalReports extends React.Component {
    constructor() {
        super();
        this.state = {
            data: [],
            data2: [],
            data3: [],
            data4:[],
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
                },() => {
                    console.log(this.state.data)});
            });
    }

    fetchINDELData() {
        fetch("http://localhost:8000/api/indel_database/")
            .then((response) => response.json())
            .then((data2) => {
                this.setState({
                    data2: data2,
                    isLoading: true,
                },() => {
                    console.log(this.state.data2)});
            });
    }

    fetchFDAData() {
        fetch("http://localhost:8000/api/fda/")
          .then((response) => response.json())
          .then((data3) => {
            this.setState({
              data3: data3,
              isLoading: true,
            },() => {
                console.log(this.state.data3)});
          });
      }

      fetchClinicalData() {
        fetch("http://localhost:8000/api/clinicaldata/")
          .then((response) => response.json())
          .then((data4) => {
            this.setState({
              data4: data4,
              isLoading: true,
            },() => {
                console.log(this.state.data4)});
          });
      }

    componentDidMount() {
        this.fetchSNVData();
        this.fetchINDELData();
        this.fetchFDAData();
        this.fetchClinicalData();
    }

    render() {
        return (
            <div>
                <h2>Final Reports</h2>
            </div>
        )
    }


}


export default FinalReports