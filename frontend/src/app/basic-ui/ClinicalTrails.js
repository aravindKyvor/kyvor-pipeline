import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Spinner } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { experimentalStyled as styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(2),
  textAlign: "center",
  color: theme.palette.text.secondary,
}));
const ClinicalTrails = () => {
  let [ClinicalTrails, setClinicalTrails] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    setInterval(function () {
      getClinicalTrails();
    }, 5000);
  }, []);

  let getClinicalTrails = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_clinicaltrails/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();

    console.log(res);
    setClinicalTrails(res);
    setLoading(false);
  };
  return !isLoading ? (
     
    <div>
      <div className="page-header">
        <h3 className="page-title">ClinicalTrails outputs </h3>
      </div>{" "}
      <br />
      <Box sx={{ flexGrow: 1 }}>
        <Grid
          container
          spacing={{ xs: 2, md: 3 }}
          columns={{ xs: 4, sm: 8, md: 12 }}
        >
      
              <Grid item xs={2} sm={4} md={4} >
                <Item>
                  
                    {ClinicalTrails[0]}
                
                </Item>
              </Grid>

              <Grid item xs={2} sm={4} md={4} >

              <Link to="/basic-ui/clinicalstudies" style={{ color: "black", textDecoration: "none" }}>
              <div
                className="card  card-img-holder text-black"
                style={{ backgroundColor: "green" }}
              >
                <Item>
                  
                 Studies
                
                </Item>
                </div>
                </Link>
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
  )
};

export default ClinicalTrails;
