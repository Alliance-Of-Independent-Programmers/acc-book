import React from "react";
import PropTypes from "prop-types";

export default function Online(props) {
  return (
    <div className="Online">
      <div className="UserInfo">
        <img className="Avatar" src={"data:image/jpeg;base64, " + props.img} />
        <div className="UserInfo-name">{props.login}</div>
      </div>
    </div>
  );
}

Online.propTypes = {
  img: PropTypes.object,
  login: PropTypes.object,
};
