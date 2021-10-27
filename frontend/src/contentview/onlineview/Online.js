import React from "react";
import PropTypes from "prop-types";

export default function Online(props) {
  return (
    <div className="Online">
      <div className="UserInfo">
        <img
          className="Avatar"
          src={"data:image/jpeg;base64, " + props.author.img}
        />
        <div className="UserInfo-name">{props.author.name}</div>
      </div>
    </div>
  );
}

Online.propTypes = {
  author: PropTypes.object,
};
