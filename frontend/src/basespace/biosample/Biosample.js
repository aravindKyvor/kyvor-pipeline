import React from "react";
import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";
// import AddIcon from "@material-ui/icons/Add";
import DeleteIcon from "@material-ui/icons/Delete";
// import EditIcon from "@material-ui/icons/Edit";
import { Spinner } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import { connect } from "react-redux";
import { getBiosample } from "../../actions/basespace";
import { toast } from "react-toastify";
class Biosample extends React.Component {
  constructor(){
    super();
    this.state={
        data:[],
        isLoaded: true,
    };
}

fetchData(){
    fetch(`${process.env.REACT_APP_API_URL}/api/biosamples/`)
    .then(response=>response.json())
    .then((data)=>{
        this.setState({
            data:data,
            isLoaded: false,
        });
        console.log(data)
    });
}









  

    componentDidMount() {
    this.timerID = setInterval(
        () =>  this.fetchData() ,
        2000
      );
    }
  
    componentWillUnmount() {
      clearInterval(this.timerID);
    }

  deleteData(id) {
    if (window.confirm("Are you sure want to delete the Biosample")) {
      fetch("http://localhost:8000/api/biosamples/" + id + "/", {
        method: "DELETE",
        body: JSON.stringify(this.state),
      })
        .then((response) => response)
        .then((data) => {
          if (data.status === 500) {
            console.log(data.status === 500);

            toast.error("Biosamples not deleted Plz check the server");
          } else {
            console.log(data);
            toast.success("Biosamples successfully deleted");
          }

          if (data) {
            this.props.getBiosample();
          }
        });
    }
  }

  render() {

    
      const biosample=this.state.data;
   
      const rows = biosample.map((item) => (
        <tr key={item.id}>
          <td>{item.biosample_id}</td>
          <td>{item.biosample_type}</td>
          <td>{item.biosample_name}</td>
          <td>{item.biosample_path}</td>
          <td>{item.library_id}</td>
          <td>{item.biosample_created_on}</td>
  
          <td>
            <DeleteIcon onClick={() => this.deleteData(item.id)} />
          </td>
        </tr>
      ));
    
    
    return !this.state.isLoaded? (
      <div>
       
        <div className="page-header">
          <h3 className="page-title">BioSampleLists </h3>
        </div>

        <div className="row">
          <div className="col-12 grid-margin">
            <div className="card">
              <div className="card-body">
                <h4 className="card-header d-flex justify-content-between align-items-center">
                  BioSample Lists
                  {/* <Link
                    to="/basespace/addbiosample"
                    style={{ textDecoration: "none" }}
                  >
                    <Button
                      variant="outlined"
                      color="secondary"
                      startIcon={<AddIcon />}
                    >
                      Add Biosample
                    </Button>
                  </Link> */}
                </h4>

                <hr />

                <div className="table-responsive">
                  <table className="table table-bordered  table-hover">
                    <thead style={{ backgroundColor: "#fec107" }}>
                      <tr>
                        <th>
                          <strong> BioSampleId</strong>
                        </th>
                        <th>
                          {" "}
                          <strong> BioSmapleType</strong>{" "}
                        </th>
                        <th>
                          {" "}
                          <strong>BioSampleName</strong>{" "}
                        </th>
                        <th>
                          {" "}
                          <strong>BioSamplePath</strong>{" "}
                        </th>
                        <th>
                          <strong>LibraryId</strong>{" "}
                        </th>
                        <th>
                          {" "}
                          <strong> Created On</strong>{" "}
                        </th>
                        <th>
                          {" "}
                          <strong>Actions</strong>{" "}
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                   {rows}
                     
                      </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    ):(
      <div className='container' style={{textAlign: 'center'}}>
      <Spinner animation="border" role="status">
              <span className="sr-only">Loading...</span>
            </Spinner>
      </div>
        )
  }
}

const mapStateToProps = (state) => ({
  biosample: state.biosample.biosample,
});

export default connect(mapStateToProps, { getBiosample })(Biosample);


