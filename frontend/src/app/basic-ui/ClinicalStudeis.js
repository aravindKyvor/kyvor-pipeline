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
const ClinicalStudies = () => {
  let [ClinicalStudies, setClinicalStudies] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    setInterval(function () {
      getClinicalStudies();
    }, 5000);
  }, []);

  let getClinicalStudies = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_clinicalstudies/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();

    console.log(res);
    setClinicalStudies(res);
    setLoading(false);
  };
  return !isLoading ? (
     
    <div>
      <div className="page-header">
        <h3 className="page-title">ClinicalStudies outputs </h3>
      </div>{" "}
      <br />
      <Box sx={{ flexGrow: 1 }}>
        <Grid
          container
          spacing={{ xs: 2, md: 3 }}
          columns={{ xs: 4, sm: 8, md: 12 }}
        >
          {ClinicalStudies.map((application, index) => {
            return (
              <Grid item xs={2} sm={4} md={4} key={index}>
                <Item>
                 
                    {application}
                
                </Item>
              </Grid>
            );
          })}
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

export default ClinicalStudies;
