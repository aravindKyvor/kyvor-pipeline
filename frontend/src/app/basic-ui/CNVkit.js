import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import FileViewer from 'react-file-viewer';

import { Spinner } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { experimentalStyled as styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import readXlsxFile from 'read-excel-file'


toast.configure();



const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(2),
  textAlign: "center",
  color: theme.palette.text.secondary,
}));
const CNVkitOutput = () => {
  let [CNV, setCNV] = useState([]);
  let[project,setproject_name]= useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    getanalysis();
  }, []);

  let getanalysis = async () => {
   
    let response = await fetch(`${process.env.REACT_APP_API_URL}/api/get_DE/`);
    let data = await response.json();

    let new_data = data.files;
    let project_name= data.project_name
    console.log(project_name)
    console.log(new_data);
    setCNV(new_data);
    setproject_name(project_name)
    setLoading(false);
  };
 
  
  return !isLoading ? (
    
    <div>
      <div className="page-header">
        <h3 className="page-title">cnvkit outputs </h3>
      </div>{" "}
      <br />
      <Box sx={{ flexGrow: 1 }}>
        <Grid
          container
          spacing={{ xs: 2, md: 3 }}
          columns={{ xs: 4, sm: 8, md: 12 }}
        >
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>
              
                {CNV[1]}
                  
                 
              </Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>
                  {/* <a  href={"/home/aravind/Desktop/DjangoProjects/djangoprojects/media/" +
          
         project+ "/DE_Outputs/TO/CNVkit_Outputs/INDKAA23695/"} download={CNV[2]} >{CNV[2]}</a> */}
         
         
         
        {CNV[2]}
         
         </Item> 
              {/* <Item>{CNV[2]}</Item> */}
            </div>
          </Grid>

          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[3]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[4]}</Item>
            </div>
          </Grid>

          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[5]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[6]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[7]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[8]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[9]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[10]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[11]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[12]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{CNV[13]}</Item>
            </div>
          </Grid>
        </Grid>
      </Box>
    </div>
  ) : (
    <div className="container" style={{ textAlign: "center" }}>
      <Spinner animation="border" role="status">
        <span className="sr-only">Loading...</span>
      </Spinner>
    </div>
  );
};

export default CNVkitOutput;
