import React from "react";
import Online from "./Online";
import PropTypes from "prop-types";

export default function CommentView(props) {
  return (
    <>
      {props.onlarr.map((comment, i) => {
        return <Online author={comment.author} key={i} />;
      })}
    </>
  );
}

CommentView.propTypes = {
  onlarr: PropTypes.array,
};
