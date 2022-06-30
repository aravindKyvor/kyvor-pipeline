import React, { useState, useEffect } from "react";

import "bootstrap/dist/css/bootstrap.min.css";
import { experimentalStyled as styled } from "@mui/material/styles";
import Paper from "@mui/material/Paper";

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === "dark" ? "#1A2027" : "#fff",
  ...theme.typography.body2,
  padding: theme.spacing(2),
  textAlign: "center",
  color: theme.palette.text.secondary,
}));
const NewProject = () => {
  let [NewProject, setNewProject] = useState([]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    setInterval(function () {
      getNewProject();
    }, 5000);
  }, []);

  let getNewProject = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_latest_project/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();

    console.log(res);
    setNewProject(res);
    setLoading(false);
  };
  return (
    <div></div>

    //     <div>
    //       <div className="page-header">
    //         <h3 className="page-title">NewProject outputs </h3>
    //       </div>{" "}
    //       <br />
    //       <Box sx={{ flexGrow: 1 }}>
    //         <Grid
    //           container
    //           spacing={{ xs: 2, md: 3 }}
    //           columns={{ xs: 4, sm: 8, md: 12 }}
    //         >
    //           {NewProject.map((application, index) => {
    //             return (
    //               <Grid item xs={2} sm={4} md={4} key={index}>
    //                 <Item>

    //                     {application}

    //                 </Item>
    //               </Grid>
    //             );
    //           })}
    //         </Grid>
    //       </Box>
    //     </div>
    //   ) : (
    //     <div className="container" style={{ textAlign: "center" }}>
    //       <Spinner animation="border" role="status">
    //         <span className="sr-only">Loading...</span>
    //       </Spinner>
    //     </div>
  );
};

export default NewProject;
