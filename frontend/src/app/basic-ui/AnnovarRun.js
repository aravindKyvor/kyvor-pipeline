import React, { useState, useEffect } from "react";
// import { Link } from "react-router-dom";
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
const Annovar = () => {
  let [Annovar, setAnnovar] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    setInterval(function () {
      getAnnovar();
    }, 5000);
  }, []);

  let getAnnovar = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_annovar/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();

    console.log(res);
    setAnnovar(res);
    setLoading(false);
  };
  return !isLoading ?(
    <div>
      <div className="page-header">
        <h3 className="page-title">Annovar outputs  </h3>
      </div>{" "}
      <br />
      <Box sx={{ flexGrow: 1 }}>
        <Grid
          container
          spacing={{ xs: 2, md: 3 }}
          columns={{ xs: 4, sm: 8, md: 12 }}
        >
          {Annovar.map((application, index) => {
            return (
              <Grid item xs={2} sm={4} md={4} key={index}>
                 <div
              className="card  card-img-holder text-black"
              style={{ backgroundColor: "#fec107" }}
            >
                <Item>
                  
                    {application}
               
                </Item>
                </div>
              </Grid>
            );
          })}
        </Grid>
      </Box>
    </div>
  ): (
    <div className="container" style={{ textAlign: "center" }}>
      <Spinner animation="border" role="status">
        <span className="sr-only">Loading...</span>
      </Spinner>
    </div>
  );
};

export default Annovar;
