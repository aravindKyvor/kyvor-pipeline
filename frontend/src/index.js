import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import App from './app/App';
import './index.css'
import * as serviceWorker from './serviceWorker';
import { transitions, positions, Provider as AlertProvider } from "react-alert";

const AlertTemplate = ({ message, options }) => {
  return (
    <div className={options.type === "success" ? "msg-success" : "msg-error"}>
      <p>{message}</p>
    </div>
  );
};

const options = {
    position: positions.TOP_RIGHT,
    timeout: 3500,
    offset: "0px",
    transition: transitions.SCALE,
  };


ReactDOM.render(
  <BrowserRouter >
      <AlertProvider template={AlertTemplate} {...options}>
    <App />
    </AlertProvider>
  </BrowserRouter>
, document.getElementById('root'));

serviceWorker.unregister();