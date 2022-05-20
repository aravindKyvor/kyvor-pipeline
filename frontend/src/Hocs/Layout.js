import React, { useEffect } from "react";
import { useLocation } from "react-router-dom";
import { connect } from "react-redux";
import { checkAuthenticated, load_user } from "../actions/auth";
import Navbar from "../app/shared/Navbar";
import Sidebar from "../app/shared/Sidebar";
import SettingsPanel from "../app/shared/SettingsPanel";
import Footer from "../app/shared/Footer";
import AppRoutes from "../app/AppRoutes";

const Layout = ({ checkAuthenticated, load_user }) => {
  useEffect(() => {
    checkAuthenticated();
    load_user();
  }, []);
  const { pathname } = useLocation();

  return (
    <div className="container-scroller">
      {pathname !== "/user-pages/login-1" && <Navbar />}

      <div className="container-fluid page-body-wrapper">
        {pathname !== "/user-pages/login-1" && <Sidebar />}
        <div className="main-panel">
       
          <div className="content-wrapper">
            
            <AppRoutes />
            <SettingsPanel />
          </div>
          
          <Footer />
        </div>
      </div>
    </div>
  );
};

export default connect(null, { checkAuthenticated, load_user })(Layout);
