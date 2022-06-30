import React from 'react'
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { Card, Button, Alert } from 'react-bootstrap'
import '../../index.css'
const ClinicalTrials = () => {
  return (
    <div>
         <Card className='Header  uvs-curve'>
        <Card.Body>
        <p style={{ textAlign: 'center' }}><strong><h3>CANLYTx® Findings</h3></strong></p>

          <div style={{ textAlign: 'center' }}>
            <strong>Clinical Trials</strong>
          </div>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead style={{ backgroundColor: "#fec107" }}>
                <TableRow>
                  <TableCell style={{
                    whiteSpace: "pre-wrap",
                    overflowWrap: "break-word",
                  }} >Biomarker</TableCell>
                  <TableCell style={{
                    whiteSpace: "pre-wrap",
                    overflowWrap: "break-word",
                  }}>Therapy</TableCell>
                  <TableCell style={{
                    whiteSpace: "pre-wrap",
                    overflowWrap: "break-word",
                  }} >
                    Variant Status in patient DNA (Variant Allele Frequency)
                  </TableCell>
                  <TableCell style={{
                    whiteSpace: "pre-wrap",
                    overflowWrap: "break-word",
                  }}>Reference</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                <TableRow

                >
                  <TableCell style={{
                    whiteSpace: "pre-wrap",
                    overflowWrap: "break-word",
                  }}>
                    EGFR (Alteration)
                  </TableCell>
                  <TableCell style={{
                    whiteSpace: "pre-wrap",
                    overflowWrap: "break-word",
                  }}>Afatinib, Cetuximab, Erlotinib, Gefitinib, Lapatinib, Panitumumab</TableCell>
                  <TableCell >Positive
                    (Copy Number 68)</TableCell>
                  <TableCell style={{
                    whiteSpace: "pre-wrap",
                    overflowWrap: "break-word",
                  }} >FDA approved for other tumour types and alterations but its utility in TNBC is not known.</TableCell>

                </TableRow>
              </TableBody>
            </Table>
          </TableContainer>
        </Card.Body>
      </Card>
    </div>
  )
}

export default ClinicalTrials