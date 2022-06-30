import React, { useEffect, useState } from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Card ,Button,Alert} from 'react-bootstrap'
const PGVUS = () => {
  const [VUS, setVUS] = useState([]);


  useEffect(() => {
    getVUS();
  }, []);

  let getVUS = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_vus/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();

    console.log(res);

    setVUS(res);

 
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
            <strong>
              {" "}
              Pharmacogenomic Biomarkers in Drug Labels - Targeted Therapies
            </strong>
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
                    Drug
                  </TableCell>
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
                    Variant status in patient
                  </TableCell>
                  
                </TableRow>
              </TableHead>
              <TableBody>
              {VUS.map((drug, index) => {
                const condition = drug.STATUS === "Positive";

                let color =
                  drug.STATUS === "Negative"
                    ? ""
                    : drug.STATUS === "Positive"
                    ? "green"
                    : "";
                  return (
                    <TableRow key={index}>
                      <TableCell
                        style={{
                          whiteSpace: "pre-wrap",
                          overflowWrap: "break-word",
                          color: condition ? "green" : "",
                        }}
                      >
                     {drug.DRUG}
                      </TableCell>
                      <TableCell
                        style={{
                          whiteSpace: "pre-wrap",
                          overflowWrap: "break-word",
                          color: condition ? "green" : "",
                        }}
                      >
                       {drug.BIOMARKER}
                      </TableCell>

                      <TableCell  style={{
                              whiteSpace: "pre-wrap",
                              overflowWrap: "break-word",

                              color: color,
                            }}
                      > {drug.STATUS}</TableCell>
                      
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

export default PGVUS;
