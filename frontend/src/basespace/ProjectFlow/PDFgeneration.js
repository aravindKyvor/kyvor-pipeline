import React, { useRef } from "react";
import { render } from "react-dom";
import { useReactToPrint } from "react-to-print";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

import BasicStack from "../PdfGeneration/Stack";
import Patient_table from "../PdfGeneration/Patient_table";
import Cantylx from "../PdfGeneration/Cantylx";
import TMB from "../PdfGeneration/TMB";
import Fda from "../PdfGeneration/Fda";

import ClinicalTrials from "../PdfGeneration/ClinicalTrials";
class PDFgeneration extends React.Component {
  render() {
    return (
      <div className="container-sm">

        <BasicStack/>

     
        <hr  style={{
            color: '#000000',
            backgroundColor:'#000000',
            height: 3}}/>
      
        {/* <div class="container">
          <h2>Panels with Contextual Classes</h2>
          <div class="panel-group">
            <div class="panel panel-default">
              <div class="panel-heading">Panel with panel-default class</div>
              <div class="panel-body">Panel Content</div>
            </div>
          </div>
        </div> */}
       
        <Patient_table/>
       
        <hr  style={{
            color: '#fec107',
            backgroundColor:' #fec107',
            height: 3}}/>

            <br/>
<Cantylx/>
<br/>

<TMB/>
<br/>
<br/>
<br/>
<br/>
<br/>


<hr/>

<small style={{textAlign: 'center',fontFamily:'Cuprum'}}>
All findings mentioned in this report are based on genomic alterations found in the tested patient’s DNA sample. 
Treating physician’s decision is final. For more information on important disclaimers please refer Annexure B.
</small>
<br/>
<br/>
<br/>
<br/>
<BasicStack/>

     
<hr  style={{
    color: '#000000',
    backgroundColor:'#000000',
    height: 3}}/>

<Fda/>

<br/>
<br/>
<br/>
<br/>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<br/>
<hr/>
<br/>
<br/>


<br/>

<BasicStack/>

     
<hr  style={{
    color: '#000000',
    backgroundColor:'#000000',
    height: 3}}/>

    <ClinicalTrials/>

        {/* <div style={{ color: "blue" }}>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell>Dessert (100g serving)
                    
                  </TableCell>
                  <TableCell align="right">Calories</TableCell>
                  <TableCell align="right">Fat&nbsp;(g)</TableCell>
                  <TableCell align="right">Carbs&nbsp;(g)</TableCell>
                  <TableCell align="right">Protein&nbsp;(g)</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                <TableRow
                  
                >
                  <TableCell component="th" scope="row">
                    Arav
                  </TableCell>
                  <TableCell align="right">dncc</TableCell>
                  <TableCell align="right">cdknc</TableCell>
                  <TableCell align="right">sow</TableCell>
                  <TableCell align="right">mi</TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </TableContainer>
        </div> */}

        <br />
        

      </div>
    );
  }
}

const Example = () => {
  const componentRef = useRef();
  const handlePrint = useReactToPrint({
    content: () => componentRef.current,
  });

  return (
    <div>
      <PDFgeneration ref={componentRef} />
      <button onClick={handlePrint}>Print this out!</button>
    </div>
  );
};

export default Example
