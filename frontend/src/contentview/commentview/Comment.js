import React from "react";
import PropTypes from "prop-types";

// function formatDate(date) {
//   return date.toLocaleDateString();
// }

export default function Comment(props) {
  return (
    <div className="Comment">
      <div className="UserInfo">
        {/*<img*/}
        {/*  className="Avatar"*/}
        {/*  src={"data:image/jpeg;base64, " + props.author.avatarUrl}*/}
        {/*  alt={props.author.name}*/}
        {/*/>*/}
        <div className="UserInfo-name">{props.author.name}</div>
      </div>
      <div className="Comment-text">{props.text}</div>
      {/*<div className="Comment-date">{formatDate(props.date)}</div>*/}
    </div>
  );
}

Comment.propTypes = {
  author: PropTypes.object,
  text: PropTypes.object,
  date: PropTypes.object,
};
