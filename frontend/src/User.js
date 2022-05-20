import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import Avatar from "react-avatar";
export class Header extends Component {
  static propTypes = {
    auth: PropTypes.object.isRequired,
  };

  render() {
    const { isAuthenticated, user } = this.props.auth;

    const authLinks = (
      <div>
        <Avatar
          color={"#fec107"}
          name={user ? `${user.first_name + " " + user.last_name}` : ""}
          maxInitials={2}
          value="86%"
          size="40"
          round="20px"
        />
      </div>
    );

    const guestLinks = "";

    return <div>{isAuthenticated ? authLinks : guestLinks}</div>;
  }
}

const mapStateToProps = (state) => ({
  auth: state.auth,
});

export default connect(mapStateToProps)(Header);
