import React from "react";
import PropTypes from "prop-types";
import UserInfo from "./UserInfo";
import Cookies from "js-cookie";

export default function UserInfoView(props) {
  return (
    <>
      <UserInfo
        img={props.user[Cookies.get("auth")].img}
        login={props.user[Cookies.get("auth")].login}
        email={props.user[Cookies.get("auth")].email}
      />
    </>
  );
}

UserInfoView.propTypes = {
  user: PropTypes.object,
};
