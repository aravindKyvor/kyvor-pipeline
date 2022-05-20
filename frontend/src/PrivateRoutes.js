import React from "react";
import { Route, Redirect } from "react-router-dom";

const PrivateRoute = ({ component: Component, ...rest }) => {
  return (
    <Route
      {...rest}
      render={(props) => {
        if (localStorage.getItem("access")) {
          return <Component {...props} />;
        } else {
          return (
            <>
              <Redirect
                to={{
                  pathname: "/user-pages/login-1",
                  state: {
                    from: props.location,
                  },
                }}
              />
            </>
          );
        }
      }}
    />
  );
};
export default PrivateRoute;
