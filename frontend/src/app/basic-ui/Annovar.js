import React from "react";
import { Form } from "react-bootstrap";
import { Link } from "react-router-dom";
const Annovar = () => {
  return (
    <div>
      <div className="page-header">
        <h3 className="page-projectName"> Analysis/Annovar</h3>
      </div>

      <div className=" col-11 grid-margin stretch-card-1 ">
        <div className="card">
          <div className="card-body">
            <form className="forms-sample">
              <Form.Group>
                <label htmlFor="exampleInputUsername1">Project Name</label>
                <Form.Control
                  type="text"
                  id="exampleInputUsername1"
                  placeholder="project Name"
                  size="lg"
                  name="projectName"
                  required
                />
              </Form.Group>

              <Form.Group>
                <label htmlFor="exampleInputUsername1">Path to VCF</label>
                <Form.Control
                  type="text"
                  id="exampleInputUsername1"
                  placeholder="Path to VCF"
                  size="lg"
                  name="projectName"
                  required
                />
              </Form.Group>

              <Form.Group>
                <label htmlFor="exampleInputUsername1">Output Path</label>
                <Form.Control
                  type="text"
                  id="exampleInputUsername1"
                  placeholder="Output Path"
                  size="lg"
                  name="projectName"
                  required
                />
              </Form.Group>

              <div className="col text-center">
                <button
                  type="submit"
                  className="btn  mr-2 btn-sm"
                  style={{ backgroundColor: "#fec107" }}
                >
                  Submit
                </button>
              </div>
            </form>
            <div className="border border-light p-3 mb-4">
              <div className="text-center">
                <span>
                  <Link to="/basic-ui/Analysis">
                    <button className="btn btn-light btn-sm"> Cancel</button>
                  </Link>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Annovar;
