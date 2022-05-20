import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { connect } from "react-redux";
import { login } from "../../actions/auth";
import axios from "axios";
import { Form } from "react-bootstrap";
import Time from "./Time";
import "../../profile.css";
const Login = ({ login, isAuthenticated }) => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const { email, password } = formData;

  const onChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = (e) => {
    e.preventDefault();

    login(email, password);
  };

  const continueWithGoogle = async () => {
    try {
      const res = await axios.get(
        `${process.env.REACT_APP_API_URL}/auth/o/google-oauth2/?redirect_uri=${process.env.REACT_APP_API_URL}/google`
      );

      window.location.replace(res.data.authorization_url);
    } catch (err) {}
  };

  if (isAuthenticated) {
    return (
      <Redirect
        to={{
          pathname: "/",
        }}
      />
    );
  }

  return (
    <div >
      <div >
        <div className="d-flex align-items-center auth px-0">
          <div className="row w-100 mx-0">
            <div className="col-lg-6 mx-auto">
              <div className="auth-form-light text-center py-5 px-4 px-sm-5">
                <div className="brand-logo">
                  <img
                    src="https://media-exp1.licdn.com/dms/image/C510BAQFzmTl0wDAz9A/company-logo_200_200/0/1571652632244?e=2159024400&v=beta&t=eaKo0GEOitZiwddxEj0nHviaJUkB3IuudN4hfCTp4fE"
                    alt="logo"
                  />
                  <div>
                    <span>
                      <Time />
                    </span>
                  </div>
                </div>
                <h4>Hello, welcome to Kyvor </h4>
                <h6 className="font-weight-light">Sign in to continue.</h6>
                <br />
                {/* <Form onSubmit={(e) => onSubmit(e)}>
                <Form.Group className="d-flex search-field">
                  <Form.Control
                    type="email"
                    placeholder="Email..."
                    size="lg"
                    className="h-auto"
                    name="email"
                    value={email}
                    onChange={(e) => onChange(e)}
                    required
                  />
                </Form.Group>
                <Form.Group className="d-flex search-field">
                  <Form.Control
                    type="password"
                    placeholder="Password"
                    size="lg"
                    className="h-auto"
                    name="password"
                    value={password}
                    onChange={(e) => onChange(e)}
                    minLength="6"
                    required
                  />
                </Form.Group>
                <div className="mt-3">
                  <button
                    className="btn btn-block btn-primary btn-sm font-weight-medium auth-form-btn"
                    type="submit"
                  >
                    SIGN IN
                  </button>
                </div>
              </Form>
              <div className="or-container">
                <div className="line-separator"></div>
                <div className="or-label">or</div>
                <div className="line-separator"></div>
              </div> */}
                <div className="pt-3">
                  <div className="mb-2">
                    <button
                      type="button"
                      className="btn btn-lg btn-social-icon-text btn-google btn-block"
                      style={{ backgroundColor: "#fec107" }}
                      onClick={continueWithGoogle}
                    >
                      <i
                        className="mdi mdi-google-plus"
                        style={{ backgroundColor: "#fec107" }}
                      ></i>
                      Google
                    </button>
                    {/* <button type="button" className="btn btn-lg btn-google btn-block text-uppercase btn-outline" onClick={continueWithGoogle}>
                     <img src="https://img.icons8.com/color/16/000000/google-logo.png"/> Signup Using Google
                    </button> */}
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

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { login })(Login);
