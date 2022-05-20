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
const PdfIchor = () => {
  let [PdfIchor, setPdfIchor] = useState([]);
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
    setPdfIchor(new_data);
    setLoading(false);
  };

  return !isLoading ? (
    <div>
      <div className="page-header">
        <h3 className="page-title">PdfIchorkit outputs </h3>
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
              <Item>{PdfIchor[34]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[35]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[36]}</Item>
            </div>
          </Grid>

          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[37]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[38]}</Item>
            </div>
          </Grid>

          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[39]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[40]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[41]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[42]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[43]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[44]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[45]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[46]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[47]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[48]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[49]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[50]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[51]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[52]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[53]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[54]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[55]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[56]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[57]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[58]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[59]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[60]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[61]}</Item>
            </div>
          </Grid>
          <Grid item xs={2} sm={4} md={4}>
            <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
              <Item>{PdfIchor[62]}</Item>
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

export default PdfIchor;
