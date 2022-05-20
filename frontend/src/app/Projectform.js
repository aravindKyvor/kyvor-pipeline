import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import Progress from "./dashboard/Progress";
import { Link } from "react-router-dom";
import axios, { post } from "axios";

import { Form } from "react-bootstrap";
import { toast } from "react-toastify";
import { Redirect } from "react-router-dom";

import "react-toastify/dist/ReactToastify.css";

const Projectform = () => {
  const [project_name, setProject_name] = useState(null);
  const [project_cancer_type, setproject_cancer_type] = useState(null);
  const [project_rerun, setproject_rerun] = useState(null);
  const [biosample_t_file1, setbiosample_t_file1] = useState("");
  const [biosample_t_file2, setbiosample_t_file2] = useState("");
 

  const [uploadPercentage, setUploadPercentage] = useState(0);

  const addPostRequest = async (e) => {
    e.preventDefault();

    setTimeout(function () {
      window.location.href = `${process.env.REACT_APP_API_URL}/basespace/pipelineresults`;
      // http://localhost:8000/basespace/projects/list
    }, 7600);

    let formField = new FormData();

    formField.append("project_name", project_name);
    formField.append("project_cancer_type", project_cancer_type);
    formField.append("project_rerun", project_rerun);
    formField.append("biosample_t_file1", biosample_t_file1);
    formField.append("biosample_t_file2", biosample_t_file2);
    

    await axios({
      method: "post",
      url: `${process.env.REACT_APP_API_URL}/api/pipeline-to`,
      headers: {
        "Content-Type": "multipart/form-data",
        "X-CSRFToken": "{{csrf_token}}",
      },

      data: formField,
      onUploadProgress: (progressEvent) => {
        setUploadPercentage(
          parseInt(
            Math.round((progressEvent.loaded * 100) / progressEvent.total)
          )
        );
        setTimeout(() => setUploadPercentage(0), 10000);
      },
    }).then(
      function (res) {
        if (res.status === 200) {
          toast.success("Project successfully deleted");
        } else if (res.status !== 200) {
          alert("Oops! ");
        }
      },
      function (res) {
        toast.error(`Request Failed`);
      }
    );
  };

  return (
    <div>
      <div className="page-header">
        <h3 className="page-title">
          <span className="page-title-icon bg-gradient-primary text-white mr-2">
            <i className="mdi mdi-home"></i>
          </span>{" "}
          Analysis Form{" "}
        </h3>
        <nav aria-label="breadcrumb">
          <ul className="breadcrumb">
            <li className="breadcrumb-data active" aria-current="page">
              <span></span>Overview{" "}
              <i className="mdi mdi-alert-circle-outline icon-sm text-primary align-middle"></i>
            </li>
          </ul>
        </nav>
      </div>

      <div className="row">
        <div className="col-12 grid-margin">
          <div>
            <div className="page-header">
              <h3 className="page-projectName"> Adding BioSample Form </h3>
              <nav aria-label="breadcrumb">
                <ol className="breadcrumb">
                  <li className="breadcrumb-item">
                    <a
                      href="!#"
                      onClick={(event) => event.preventDefault()}
                    ></a>
                  </li>
                </ol>
              </nav>
            </div>

            <div className=" col-11 grid-margin stretch-card-1 ">
              <div className="card">
                <div className="card-body">
                  <Form.Group>
                    <label htmlFor="projectname">project_name</label>

                    <Form.Control
                      value={project_name}
                      name="project_name"
                      onChange={(e) => setProject_name(e.target.value)}
                      type="text"
                      id="projectname"
                      placeholder="project_name"
                      size="lg"
                      required
                    />
                  </Form.Group>
                  <Form.Group>
                    <label htmlFor="projectcancertype">
                      project_cancer_type
                    </label>
                    <Form.Control
                      type="text"
                      id="projectcancertype"
                      placeholder="BioSample Type"
                      size="lg"
                      defaultValue="Solid Tumor, Metastatic Cancer"
                      value={project_cancer_type}
                      name="project_cancer_type"
                      onChange={(e) => setproject_cancer_type(e.target.value)}
                      required
                    />
                  </Form.Group>
                  <Form.Group>
                    <label id="project_rerun">project_rerun</label>
                    <input
                      type="text"
                      className="form-control"
                      id="project_rerun"
                      placeholder="BioSample Name"
                      value={project_rerun}
                      name="project_rerun"
                      onChange={(e) => setproject_rerun(e.target.value)}
                      required
                    />
                  </Form.Group>
                  <Form.Group>
                    <label id="biosample_t_file1">biosample_t_file1</label>
                    <Form.Control
                      type="file"
                      placeholder="BioSample Path"
                      onChange={(e) => setbiosample_t_file1(e.target.files[0])}
                      required
                    />
                  </Form.Group>
                  <Progress percentage={uploadPercentage} />
                  <Form.Group>
                    <label id="biosample_t_file2">biosample_t_file2</label>
                    <Form.Control
                      type="file"
                      placeholder="BioSample Path"
                      onChange={(e) => setbiosample_t_file2(e.target.files[0])}
                      required
                    />
                  </Form.Group>
                  <Progress percentage={uploadPercentage} />
                 
                  

                  {/* <FormControl
                name="project_id"
                componentClass="select"
                onChange={this.on}
              >
                {userlist.map((r, i) => (
                  <option key={i} value={r.id}>
                    {r.name}
                  </option>
                ))}
              </FormControl> */}

                  <div className="col text-center">
                    <button
                      type="submit"
                      onClick={addPostRequest}
                      className="btn  mr-2 btn-sm"
                      style={{ backgroundColor: "#fec107" }}
                    >
                      Submit
                    </button>
                  </div>

                  <div className="border border-light p-3 mb-4">
                    <div className="text-center">
                      <span>
                        <Link to="/basic-ui/Basespace">
                          <button className="btn btn-light btn-sm">
                            {" "}
                            Cancel
                          </button>
                        </Link>
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Projectform;
