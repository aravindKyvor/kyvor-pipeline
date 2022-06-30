// import React, { useState, useEffect, Fragment } from "react";
// import { Table } from "react-bootstrap";
// import { Spinner } from "react-bootstrap";
// import axios from 'axios'
// import { ProgressBar } from "react-bootstrap";
// import DeleteIcon from "@material-ui/icons/Delete";

// const ClinicalStudies = () => {
//   let [studies, setstudies] = useState([]);
//   const [isLoading, setLoading] = useState(true);


//   useEffect(() => {
//     // setInterval(function () {
//     getstudies();
//     // }, 2000);
//   }, []);
//   let getstudies = async () => {
//     let response = await fetch(
//       `${process.env.REACT_APP_API_URL}/api/clinicaldata/`
//     );
//     let data = await response.json();

//     console.log(data);
//     setstudies(data);
//     setLoading(false);
//   };

//   const removeData = (id) => {
//     let URL = `${process.env.REACT_APP_API_URL}/api/clinicaldata/`
//     axios.delete(`${URL}/${id}`).then(res => {
//       const del = studies.filter(study => id !== study.id)
//       setstudies(del);
//     })
//   }

//   return !isLoading ? (
//     <div>
//       <div className="col-lg-12 grid-margin">
//         <div className="card">
//           <div className="card-body">
//             <h4 className="card-title">Clinical & Case Studies </h4>
//             <div className="table-wrapper-scroll-y my-custom-scrollbar">
//             <div className="table-responsive">
//               <table
//                 className="table table-bordered text-wrap"
//                 style={{ width: "auto" }}
//               >
//                 <tr>
//                 <th style={{ backgroundColor: "#fec107" }}>
//          #
//         </th>
//                   <th style={{ backgroundColor: "#fec107" }}>Biomarker</th>

//                   <th style={{ backgroundColor: "#fec107" }}>Therapy</th>
//                   <th
//                     style={{
//                       backgroundColor: "#fec107",
//                       whiteSpace: "pre-wrap",
//                       overflowWrap: "break-word",
//                     }}
//                   >
//                     {" "}
//                     Variant Status in patient DNA (Variant Allele Frequency)
//                   </th>
//                   <th style={{ backgroundColor: "#fec107" }}>Reference</th>
//                 </tr>
//                 {studies.map((application, index) => {
//                   return (
//                     <Fragment>
//                       <tr key={index}>
//                        <td rowspan="2">
//                        <DeleteIcon onClick={() => removeData(application.id)} />
//                        </td>
//                         <td rowspan="2">{application.BioMarker}</td>



//                         <td
//                           style={{
//                             whiteSpace: "pre-wrap",
//                             overflowWrap: "break-word",
//                           }}
//                         >
//                           {application.intervention}
//                         </td>
//                         <td
//                           style={{

//                             textAlign: "left",
//                           }}
//                         >
//                           {application.Status}
//                         </td>
//                         <td
//                           style={{
//                             // whiteSpace: "pre-wrap",
//                             overflowWrap: "break-word",
//                             textAlign: "left",
//                           }}
//                         >
//                           <a href={application.url} target="_blank" rel="noopener noreferrer"
//                             className="btn btn-link"
//                             style={{ textDecoration: "none" }}
//                           > {application.Reference}</a>
//                         </td>
//                       </tr>

//                       <tr>
//                         <td
//                           colspan="4"
//                           style={{
//                             whiteSpace: "pre-wrap",
//                             textAlign: "center",
//                           }}
//                         >
//                           {application.official_title}
//                         </td>
//                       </tr>
//                     </Fragment>
//                   );
//                 })}
//               </table>
//             </div>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   ) : (
//     //     </div>
//     //   </div>
//     // </div>
//     <div className="container" style={{ textAlign: "center" }}>
//       <Spinner animation="border" role="status">
//         <span className="sr-only">Loading...</span>
//       </Spinner>
//     </div>
//   );
// };

// export default ClinicalStudies;

import { Spinner } from "react-bootstrap";


import React from "react";
import { Link } from "react-router-dom";
import Button from "@material-ui/core/Button";
import AddIcon from "@material-ui/icons/Add";
import DeleteIcon from "@material-ui/icons/Delete";
import EditIcon from "@material-ui/icons/Edit";
import { ToastContainer, toast } from "react-toastify";
class ClinicalStudies extends React.Component {
  constructor() {
    super();
    this.state = {
      data: [],
      isLoading: false,
    };
  }

  fetchData() {
    fetch("http://localhost:8000/api/clinicaldata/")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          data: data,
          isLoading: true,
        });
      });
  }

  componentDidMount() {
    this.fetchData();
  }

  deleteData(id) {
    if (window.confirm("Are you sure want to delete the Clinical datas")) {
      fetch("http://localhost:8000/api/clinicaldata/" + id + "/", {
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
            toast.error("Clinical data was not deleted", {
              position: "top-right",
              autoClose: 2000,
            });
          }
        });
    }
  }

  render() {
    const { isLoading } = this.state;
    const ClinicalData = this.state.data;
    const rows = ClinicalData.map((application) => (
      <div>
        <tr key={application.id}>

          <td rowspan="2">
            <DeleteIcon onClick={() => this.deleteData(application.id)} />


          </td>
          <td rowspan="2">{application.BioMarker}</td>



          <td
            style={{
              whiteSpace: "pre-wrap",
              overflowWrap: "break-word",
            }}
          >
            {application.intervention}
          </td>
          <td
            style={{

              textAlign: "left",
            }}
          >
            {application.Status}
          </td>
          <td
            style={{
              // whiteSpace: "pre-wrap",
              overflowWrap: "break-word",
              textAlign: "left",
            }}
          >
            <a href={application.url} target="_blank" rel="noopener noreferrer"
              className="btn btn-link"
              style={{ textDecoration: "none" }}
            > {application.Reference}</a>
          </td>
        </tr>

        <tr>
          <td
            colspan="4"
            style={{
              whiteSpace: "pre-wrap",
              textAlign: "center",
            }}
          >
            {application.official_title}
          </td>
        </tr>
      </div>
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
                <div className="col-12 grid-margin">
                  <div className="card">
                    <div className="card-body">
                      <h4 className="card-header d-flex justify-content-between align-items-center">
                        Clinical & Case Studies                      </h4>

                      <hr />
                      <div className="table-wrapper-scroll-y my-custom-scrollbar">
                        <div className="table-responsive">
                          <table className="table table-bordered">

                            <thead style={{ backgroundColor: "#fec107" }}>
                              <div>
                                <tr>
                                  <th style={{ backgroundColor: "#fec107" }}>
                                    #
                                  </th>
                                  <th style={{ backgroundColor: "#fec107" }}>Biomarker</th>

                                  <th style={{ backgroundColor: "#fec107" }}>Therapy</th>
                                  <th
                                    style={{
                                      backgroundColor: "#fec107",
                                      whiteSpace: "pre-wrap",
                                      overflowWrap: "break-word",
                                    }}
                                  >
                                    {" "}
                                    Variant Status in patient DNA (Variant Allele Frequency)
                                  </th>
                                  <th style={{ backgroundColor: "#fec107" }}>Reference</th>
                                </tr>
                              </div>
                            </thead>
                            <tbody>{rows}</tbody>
                          </table>
                        </div>
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

export default ClinicalStudies;
