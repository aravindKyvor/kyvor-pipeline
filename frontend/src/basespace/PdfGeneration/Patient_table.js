import React from 'react'
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { backdropClasses } from '@mui/material';
import color from '@material-ui/core/colors/amber';

const Patient_table = () => {
  return (
    <div style={{fontFamily:'Cuprum'}}>
        <React.Fragment>
      


                <TableContainer component={Paper}  >
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
              <TableHead>
                <TableRow>
                  <TableCell  style={{backgroundColor:'#D0D0D0'}}>Patient Information </TableCell>
                  <TableCell style={{backgroundColor:'#FFFFFF'}} >
                 INDTSA54969 | F | 73 Yrs | Mrs. A Renuka Devi
                  </TableCell>
                
                </TableRow>
                <TableRow>
                  <TableCell  style={{backgroundColor:'#D0D0D0'}}>Physician Information </TableCell>
                  
                  <TableCell style={{backgroundColor:'#FFFFFF'}} >
                 INDTS00101 | Dr. P S Dattatreya
                  </TableCell>
                </TableRow>
                <TableRow  >
                  <TableCell style={{backgroundColor:'#D0D0D0'}}>Specimen </TableCell>
                  <TableCell style={{backgroundColor:'#FFFFFF'}} >
                 Carcinoma Ascending Colon
                  </TableCell>
                
                </TableRow>
                <TableRow>
                  <TableCell  style={{backgroundColor:'#D0D0D0'}}>Cancertype </TableCell>
                  <TableCell  style={{backgroundColor:'#FFFFFF'}}>
                Type - FFPE Block | ID - 4152A(7/8/9)/21 | Site - Right Colon
                  </TableCell>
                
                </TableRow>
              </TableHead>
            
            </Table>
          </TableContainer>
            
    

       
        </React.Fragment>
    </div>
  )
}

export default Patient_table