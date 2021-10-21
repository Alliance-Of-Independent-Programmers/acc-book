import React from "react";
import Comment from "./Comment";
import PropTypes from "prop-types";

export default function CommentView(props) {
  return (
    <>
      {props.comments.map((comment, i) => {
        return (
          <Comment
            date={comment.date}
            text={comment.text}
            author={comment.author}
            key={i}
          />
        );
      })}
    </>
  );
}

CommentView.propTypes = {
  comments: PropTypes.array,
};
