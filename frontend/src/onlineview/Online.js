import React from "react";
import PropTypes from "prop-types";

fetch("/api/online.json")
    .then(res => res.json())
    .then(onlarr => )


export default function Online(props) {
  return (
    <div className="Online">
      <div className="UserInfo">
        <img
          className="Avatar"
          src={props.author.avatarUrl}
          alt={props.author.name}
        />
        <div className="UserInfo-name">{props.author.name}</div>
      </div>
    </div>
  );
}

Online.propTypes = {
  author: PropTypes.object,
};
