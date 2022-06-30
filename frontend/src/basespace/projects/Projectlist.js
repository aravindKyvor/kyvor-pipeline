import React from "react";

import DeleteIcon from "@material-ui/icons/Delete";

import { toast } from "react-toastify";

import "react-toastify/dist/ReactToastify.css";

toast.configure();

class ProjectList extends React.Component {
  constructor() {
    super();
    this.state = {
      data: [],
    };
  }

  fetchData() {
    fetch(`${process.env.REACT_APP_API_URL}/api/projects/`)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          data: data,
        });
        console.log(data)
      });
  }

  componentDidMount() {
    this.fetchData();

    setTimeout(function () {
      window.location.href = `${process.env.REACT_APP_API_URL}/basespace/analysis/`;
    }, 5000);
  }

  deleteData(id) {
    if (window.confirm("Are you sure want to delete the Project")) {
      fetch(`${process.env.REACT_APP_API_URL}/api/project/` + id + "/", {
        method: "DELETE",
        body: JSON.stringify(this.state),
      })
        .then((response) => response)
        .then((data) => {
          if (data.status === 500) {
            console.log(data.status === 500);

            toast.error(
              "Project has been used by some other application! You cannot delete it"
            );
          } else {
            console.log(data);
            toast.success("Project successfully deleted");
          }

          if (data) {
            this.props.getProject();
          }
        });
    }
  }
  render() {
    const project = this.state.data;
    const rows = project.map((item) => (
      <tr key={item.id}>
        <td>{item.project_name}</td>
        <td>{item.bs_default_project}</td>
        <td>{item.bs_project_id}</td>
        <td>{item.project_type}</td>
        <td>{item.project_created_on}</td>
        <td>{item.bs_user_id}</td>

        <td>
          <DeleteIcon onClick={() => this.deleteData(item.id)} />
        </td>
      </tr>
    ));
    return (
      <div>
        <div className="page-header">
          <h3 className="page-title">Project Lists </h3>
        </div>

        <div className="row">
          <div className="col-12 grid-margin">
            <div className="card">
              <div className="card-body">
                <h4 className="card-header d-flex justify-content-between align-items-center">
                  Project Lists
                </h4>

                <hr />

                <div className="table-responsive">
                  <table className="table table-bordered  table-hover">
                    <thead style={{ backgroundColor: "#fec107" }}>
                      <tr>
                        <th>
                          <strong> Project Name</strong>
                        </th>
                        <th>
                          {" "}
                          <strong> BS Default Project</strong>{" "}
                        </th>
                        <th>
                          {" "}
                          <strong>Bs Project ID</strong>{" "}
                        </th>
                        <th>
                          {" "}
                          <strong>Project Type</strong>{" "}
                        </th>
                        <th>
                          <strong> Project Created On</strong>{" "}
                        </th>
                        <th>
                          {" "}
                          <strong> Bs User Id</strong>{" "}
                        </th>
                        <th colSpan="2">
                          {" "}
                          <strong>Actions</strong>{" "}
                        </th>
                      </tr>
                    </thead>
                    <tbody>{rows}</tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default ProjectList;
