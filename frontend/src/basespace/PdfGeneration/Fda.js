import React,{useState,useEffect} from "react";
import Table from "@mui/material/Table";

import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Card, Button, Alert } from "react-bootstrap";
import '../../index.css'
const Fda = () => {
  let [fda, setfda] = useState([]);

  useEffect(() => {
    getfda();
  }, []);

  let getfda = async () => {
    let response = await fetch(`${process.env.REACT_APP_API_URL}/api/fda/`);
    let data = await response.json();
   
    // console.log(data)
    console.log(data);
    setfda(data);
  };
  return (
    <div>
      <Card className="Header  uvs-curve">
        <Card.Body>
          <p style={{ textAlign: "center" }}>
            <strong>
              <h3>CANLYTx® Findings</h3>
            </strong>
          </p>
          <div style={{ textAlign: "center" }}>
            <strong> FDA Approved Recommendations - Patient Cancer type</strong>
          </div>

          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead style={{ backgroundColor: "#fec107" }}>
                <TableRow>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    Biomarker
                  </TableCell>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    Therapy
                  </TableCell>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    Variant Status in patient DNA (Variant Allele Frequency)
                  </TableCell>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    AF_VAF
                  </TableCell>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    Reference
                  </TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                <TableRow>
                  <TableCell>
                    No FDA approved biomarkers identified in this patient{" "}
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </TableContainer>
          <br />
          <br />

          <div style={{ textAlign: "center" }}>
            <strong>FDA Approved Recommendations - Other Cancer type</strong>
          </div>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead style={{ backgroundColor: "#fec107" }}>
                <TableRow>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    Biomarker
                  </TableCell>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    Therapy
                  </TableCell>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    Variant Status in patient DNA (Variant Allele Frequency)
                  </TableCell>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    AF_VAF
                  </TableCell>
                  <TableCell
                    style={{
                      whiteSpace: "pre-wrap",
                      overflowWrap: "break-word",
                    }}
                  >
                    Reference
                  </TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {fda.map((item, index) => {
                  return (
                    <TableRow key={index}>
                      <TableCell
                        style={{
                          whiteSpace: "pre-wrap",
                          overflowWrap: "break-word",
                        }}
                      >
                      {item.BIOMARKER}
                      </TableCell>
                      <TableCell
                        style={{
                          whiteSpace: "pre-wrap",
                          overflowWrap: "break-word",
                        }}
                      >
                        {item.THERAPY}
                      </TableCell>

                      <TableCell>{item.Status}</TableCell>
                      <TableCell> {item.AF_VAF}</TableCell>
                      <TableCell
                        style={{
                          whiteSpace: "pre-wrap",
                          overflowWrap: "break-word",
                        }}
                      >
                         {item.EVIDENCE_STATEMENT_1}
                      </TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            </Table>
          </TableContainer>
        </Card.Body>
      </Card>
    </div>
  );
};

export default Fda;

// import { Spinner } from "react-bootstrap";

// // import React from "react";
// import { Link } from "react-router-dom";
// import Button from "@material-ui/core/Button";
// import AddIcon from "@material-ui/icons/Add";
// import DeleteIcon from "@material-ui/icons/Delete";
// import EditIcon from "@material-ui/icons/Edit";
// import { ToastContainer, toast } from "react-toastify";
// class Fda extends React.Component {
//   constructor() {
//     super();
//     this.state = {
//       data: [],
//       isLoading: false,
//     };
//   }

//   fetchData() {
//     fetch("http://localhost:8000/api/fda/")
//       .then((response) => response.json())
//       .then((data) => {
//         this.setState(
//           {
//             data: data,
//             isLoading: true,
//           },
//           () => {
//             console.log(this.state.data);
//           }
//         );
//       });
//   }

//   componentDidMount() {
//     this.fetchData();
//   }

//   render() {
//     const { isLoading } = this.state;
//     const fdaData = this.state.data;
//     const rows = fdaData.map((item) => (
//       <tr key={item.id}>
//         <td style={{ whiteSpace: "pre-wrap", overflowWrap: "break-word" }}>
//           {" "}
//           {item.BIOMARKER}
//         </td>
//         <td> {item.THERAPY}</td>

//         <td style={{ whiteSpace: "pre-wrap", overflowWrap: "break-word" }}>
//           {" "}
//           {item.Status}
//         </td>
//         <td style={{ whiteSpace: "pre-wrap", overflowWrap: "break-word" }}>
//           {" "}
//           {item.AF_VAF}
//         </td>
//         <td style={{ whiteSpace: "pre-wrap", overflowWrap: "break-word" }}>
//           {" "}
//           {item.EVIDENCE_STATEMENT_1}
//         </td>

//       </tr>
//     ));
//     return (
//       <React.Fragment>
//         {!isLoading ? (
//           <div className="container" style={{ textAlign: "center" }}>
//             <Spinner animation="border" role="status">
//               <span className="sr-only">Loading...</span>
//             </Spinner>
//           </div>
//         ) : (
//           <div>
//             <div className="row">
//               <div className="col-12 grid-margin">
//                 <div className="card">
//                   <div className="card-body">
//                     <h4 className="card-title">
//                       {" "}
//                       FDA Approved Recommendations - Patient Cancer type
//                     </h4>
//                     <div className="table-responsive">
//                       <table
//                         className="table table-bordered text-wrap"
//                         style={{ width: "auto" }}
//                       >
//                         {" "}
//                         <thead style={{ backgroundColor: "#fec107" }}>
//                           <tr>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               Biomarker
//                             </th>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               Therapy
//                             </th>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               {" "}
//                               Variant Status in patient DNA (Variant Allele
//                               Frequency)
//                             </th>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               Reference
//                             </th>
//                           </tr>
//                         </thead>
//                         <tbody>
//                           No FDA approved biomarkers identified in this patient
//                         </tbody>
//                       </table>
//                     </div>
//                   </div>
//                 </div>
//               </div>
//             </div>
//             <div className="row">
//               <div className="col-12 grid-margin">
//                 <div className="card">
//                   <div className="card-body">
//                     <h4 className="card-header d-flex justify-content-between align-items-center">
//                       FDA Approved Recommendations - Patient Cancer type
//                     </h4>

//                     <hr />

//                     <div className="table-responsive">
//                       <Table className="table table-bordered  table-hover">
//                         <thead style={{ backgroundColor: "#fec107" }}>
//                           <tr>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               <strong>BioMarker</strong>
//                             </th>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               <strong>THERAPY</strong>
//                             </th>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               <strong>Status</strong>
//                             </th>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               <strong>AF_VAF</strong>
//                             </th>
//                             <th
//                               style={{
//                                 whiteSpace: "pre-wrap",
//                                 overflowWrap: "break-word",
//                               }}
//                             >
//                               <strong>EVIDENCE_STATEMENT_1</strong>
//                             </th>

//                           </tr>
//                         </thead>
//                         <tbody>{rows}</tbody>
//                       </Table>
//                     </div>
//                   </div>
//                 </div>
//               </div>
//             </div>
//           </div>
//         )}
//       </React.Fragment>
//     );
//   }
// }

// export default Fda;
