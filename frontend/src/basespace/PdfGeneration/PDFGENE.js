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
import BasicStack from "./Stack";
import Patient_table from "./Patient_table";
import Cantylx from "./Cantylx";
import TMB from "./TMB";
import Fda from "./Fda";
import "../../index.css";
import { Button } from "bootstrap";
import ClinicalTrials from "./ClinicalTrials";
import Print from "./Print";
import logo1 from "./kyvor_logo.png";
import logo2 from "./cantylx.png";
import { Navbar, Container } from "react-bootstrap";
import GenomicSummary from "../ProjectFlow/GenomicSummary";
// import Vus from "../ProjectFlow/Vus";
import { Card } from "@material-ui/core";
import PGVUS from "./PGVUS";
class ComponentToPrint extends React.Component {
  render() {
    return (
      <div className="container-sm">
        <br />
        <br />
        <BasicStack />
        <hr
          style={{
            color: "#000000",
            backgroundColor: "#000000",
            height: 3,
          }}
        />

        {/* <div class="container">
          <h2>Panels with Contextual Classes</h2>
          <div class="panel-group">
            <div class="panel panel-default">
              <div class="panel-heading">Panel with panel-default class</div>
              <div class="panel-body">Panel Content</div>
            </div>
          </div>
        </div> */}

        <Patient_table />

        <hr
          style={{
            color: "#fec107",
            backgroundColor: " #fec107",
            height: 3,
          }}
        />

        <br />
        <Cantylx />
        <br />

        <TMB />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <hr />

        <small style={{ textAlign: "center", fontFamily: "Cuprum" }}>
          All findings mentioned in this report are based on genomic alterations
          found in the tested patient’s DNA sample. Treating physician’s
          decision is final. For more information on important disclaimers
          please refer Annexure B.
        </small>
        <br />
        <br />
        <br />
        <br />
        <BasicStack />

        <hr
          style={{
            color: "#000000",
            backgroundColor: "#000000",
            height: 3,
          }}
        />

        <Fda />

        <br />
        <br />
        <br />
        <br />

        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />

        <br />

        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <hr />
        <br />
        <br />
        <br />
        

        <BasicStack />

        <hr
          style={{
            color: "#000000",
            backgroundColor: "#000000",
            height: 3,
          }}
        />

        <ClinicalTrials />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />

        <br />

        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />

        <br />

        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />

        <br />

        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />

        <br />

        <br />
        <br />
        <br />

        <br />

        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br/>
        <br/>
        <br/>
        <BasicStack />

        <hr
          style={{
            color: "#000000",
            backgroundColor: "#000000",
            height: 3,
          }}
        />
       
       
       <div>
       <GenomicSummary />

        </div> 

       
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        
        <br/>
        
       
        <BasicStack />

        <hr
          style={{
            color: "#000000",
            backgroundColor: "#000000",
            height: 3,
          }}
        />
        <PGVUS/>
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
       <button onClick={handlePrint}>Print this out!</button>
      <ComponentToPrint ref={componentRef} />
     
    </div>
  );
};

export default Example;
