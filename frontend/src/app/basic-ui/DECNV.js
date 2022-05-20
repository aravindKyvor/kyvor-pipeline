import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { Spinner } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { experimentalStyled as styled } from "@mui/material/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
toast.configure();
const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(2),
  textAlign: "center",
  color: theme.palette.text.secondary,
}));
const DECnv = () => {
  let [DECnv, setDECnv] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    getanalysis();
  }, []);

  let getanalysis = async () => {
    let response = await fetch(`${process.env.REACT_APP_API_URL}/api/get_DE/`);
    let data = await response.json();

    let new_data = data.files;
    // console.log(data)
    console.log(new_data);
    setDECnv(new_data);
    setLoading(false);
  };

  return !isLoading ? (
    <div>
      <div className="page-header">
        <h3 className="page-title">DE CNV curation  outputs </h3>
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
              <Item>{DECnv[14]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[15]}</Item>
            </div>
          </Grid>

          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[16]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[17]}</Item>
            </div>
          </Grid>

          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[18]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[19]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[20]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[21]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[22]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[23]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{DECnv[24]}</Item>
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

export default DECnv;
