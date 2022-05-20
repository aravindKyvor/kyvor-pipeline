import React, { useEffect } from "react";
import { Link, useLocation, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import { googleAuthenticate } from "../../actions/auth";
import queryString from "query-string";

const Google = ({ googleAuthenticate, isAuthenticated }) => {
  let location = useLocation();

  useEffect(() => {
    const values = queryString.parse(location.search);
    const state = values.state ? values.state : null;
    const code = values.code ? values.code : null;

    console.log("State: " + state);
    console.log("Code: " + code);

    if (state && code) {
      googleAuthenticate(state, code);
    }
  }, [location]);

  if (isAuthenticated) {
    return (
      <Redirect
        to={{
          pathname: "/",
        }}
      />
    );
  } else if (!isAuthenticated) {
    return (
      <Redirect
        to={{
          pathname: "/user-pages/login-1",
        }}
      />
    );
  }

  return <div></div>;
};

export default connect(null, { googleAuthenticate })(Google);
