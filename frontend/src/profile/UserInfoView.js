import React from "react";
import PropTypes from "prop-types";
import UserInfo from "./UserInfo";

export default function UserInfoView(props) {
  return (
    <>
      {props.onlarr.map((online, i) => {
        return (
          <UserInfo
            img={online.img}
            login={online.login}
            email={online.email}
            key={i}
          />
        );
      })}
    </>
  );
}

UserInfoView.propTypes = {
  onlarr: PropTypes.array,
};
