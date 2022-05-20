import React, { useState, useEffect } from "react";

const Tnpipeline = () => {
  let [getTNvalues, setgetTNvalues] = useState([]);
  let [whomai, setWhoami] = useState([]);
  let [validateProject, setValidateProject] = useState([]);
  let[reqProjects,setreqProjects] = useState([]);
  let[datauploads,setdatauploads] = useState([]);

  let[uploadCommand,setuploadCommand] = useState([]);
  let[reqdata,setreqdata] = useState([]);
 

  useEffect(() => {
    setInterval(function () {
      getWhomai();
    getgetTNvalues();
    }, 5000);
  }, []);

  let getgetTNvalues = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_results/`
    );
    let data = await response.json();
    console.log(data)
    let projectdata = data.validateProject;
    let reqProject=data.req_projects
    let reqs= data.req
    let uploaddata = data.upload_cmd
    let dataupload = data.data_upload
    console.log(projectdata);
    setValidateProject(projectdata);
    setreqProjects(reqProject)
    setreqdata(reqs)
    setuploadCommand(uploaddata)
    setdatauploads(dataupload)
  };

  let getWhomai = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_whoami/`
    );
    let data = await response.json();

    console.log(data);
    setWhoami(data);
  };
  return (
    <div className="row">
      <div className="col-lg-12 grid-margin stretch-card">
        <div className="card text-center">
          <div className="card-body">
            <h4 className="card-title">WhoAmi</h4>
            <div className="alert alert-success">{whomai}</div>
          </div>
        </div>
      </div>

      <br></br>
     
      <div className="col-lg-12 grid-margin stretch-card">
        <div className="card text-center">
          <div className="card-body">
            <h4 className="card-title">Upload Status</h4>
           {reqProjects.map((data,index)=>{
               return(
                   <div key={index}>
                       {data}
                   </div>
               )
           })}
          </div>
        </div>
      </div>

    

  



      {/* <div className="col-lg-12 grid-margin stretch-card">
        <div className="card text-center">
          <div className="card-body">
            <h4 className="card-title">Upload Status</h4>
            code:{validateProject.Code},   <br></br>
            Message:{validateProject.Message}<br></br>
            Reference:{validateProject.Reference}<br></br>
            Status:{validateProject.Status}<br></br>
            Type:{validateProject.Type ? "true" : "false"}
          </div>
        </div>
      </div>
 */}



      <div className="col-lg-12 grid-margin stretch-card">
        <div className="card text-center">
          <div className="card-body">
            <h4 className="card-title">Upload Status</h4>
           {reqdata.map((data,index)=>{
               return(
                   <div key={index}>
                       {data}
                   </div>
               )
           })}
          </div>
        </div>
      </div>

      <div className="col-lg-12 grid-margin stretch-card">
        <div className="card text-center">
          <div className="card-body">
            <h4 className="card-title">Upload Status</h4>
          {uploadCommand}
          </div>
        </div>
      </div>


      <div className="col-lg-12 grid-margin stretch-card">
        <div className="card text-center">
          <div className="card-body">
            <h4 className="card-title">Upload Status</h4>
          {datauploads}
          </div>
        </div>
      </div>

    </div>
  );
};

export default Tnpipeline;
