import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import "./App.scss";
import Layout from "../Hocs/Layout";
import { Provider } from "react-redux";
import store from "../store";
class App extends Component {
  render() {
    return (
      <div>
        <Provider store={store}>
          <Layout />
        </Provider>
      </div>
    );
  }
}
export default withRouter(App);
