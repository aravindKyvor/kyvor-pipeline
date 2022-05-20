import React, { Component, Fragment } from "react";
import { Dropdown } from "react-bootstrap";
import { Link } from "react-router-dom";
import {AppBar, Button, Menu, MenuItem, Toolbar} from "@mui/material";
import {BsCardList, BsPerson} from "react-icons/bs";
import User from "../../User";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { logout } from "../../actions/auth";

class Navbar extends Component {
  static propTypes = {
    auth: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired,
  };
  toggleOffcanvas() {
    document.querySelector(".sidebar-offcanvas").classList.toggle("active");
  }
  toggleRightSidebar() {
    document.querySelector(".right-sidebar").classList.toggle("open");
  }
  render() {
    const { isAuthenticated,user } = this.props.auth;

    
 
  
    return (
      <nav className="navbar default-layout-navbar col-lg-12 col-12 p-0 fixed-top d-flex flex-row">
        <div className="text-center navbar-brand-wrapper d-flex align-items-center justify-content-center">
          <Link className="navbar-brand brand-logo" to="/">
            <img
              src="https://media-exp1.licdn.com/dms/image/C510BAQFzmTl0wDAz9A/company-logo_200_200/0/1571652632244?e=2159024400&v=beta&t=eaKo0GEOitZiwddxEj0nHviaJUkB3IuudN4hfCTp4fE"
              alt="logo"
            />
          </Link>
          <Link className="navbar-brand brand-logo-mini" to="/">
            <img
              src="https://pbs.twimg.com/profile_images/916670511463071744/RUxkG06c_400x400.jpg"
              alt="logo"
            />
          </Link>
        </div>
        <div className="navbar-menu-wrapper d-flex align-items-stretch">
          <button
            className="navbar-toggler navbar-toggler align-self-center"
            type="button"
            onClick={() => document.body.classList.toggle("sidebar-icon-only")}
          >
            <span className="mdi mdi-menu"></span>
          </button>

          {isAuthenticated ? (
            <Fragment>


      
         
          <div className="flex-grow-1"/>

          
    
              <ul className="navbar-nav navbar-nav-right">
                <li className="nav-item nav-profile">
                  <Dropdown alignRight>
                  

               





                   <Dropdown.Toggle   variant="link" bsPrefix="p-0" className="nav-link">
                  
                   <Button endIcon={<BsPerson    style={{justifyContent: 'center',
                      alignItems: 'center',}}  />}
                      style={{justifyContent: 'center',
                      alignItems: 'center',}}
                      size="large"
                      aria-label="account of current user"
                      aria-controls="menu-appbar"
                      aria-haspopup="true"
                    
                     
                  
                    >
                    
                    
                     
              
              {user ? `${user.first_name}` : ""}


              
              </Button> 
                     

                      
                    </Dropdown.Toggle> 

                    <Dropdown.Menu className="navbar-dropdown" >
                      <Dropdown.Item>
                        <i className="mdi mdi-logout mr-2 text-primary"></i>
                      
                          {" "}
                          <Link
                            to="/user-pages/login-1"
                            onClick={this.props.logout}
                          >
                            Signout
                          </Link>
                        
                      </Dropdown.Item>
                    </Dropdown.Menu>
                  </Dropdown>
                </li>
              </ul>
            </Fragment>
          ) : (
            <Fragment></Fragment>
          )}

          <button
            className="navbar-toggler navbar-toggler-right d-lg-none align-self-center"
            type="button"
            onClick={this.toggleOffcanvas}
          >
            <span className="mdi mdi-menu"></span>
          </button>
        </div>
      </nav>
    );
  }
}

const mapStateToProps = (state) => ({
  auth: state.auth,
});

export default connect(mapStateToProps, { logout })(Navbar);
