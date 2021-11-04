import React from "react";
import Comment from "./Comment";
import PropTypes from "prop-types";
import Col from "react-bootstrap/Col";

export default function CommentView(props) {
  return (
    <Col xs={9}>
      {props.comments.map((comment, i) => {
        return (
          <Comment
            date={comment.date}
            text={comment.text}
            img={comment.img}
            login={comment.login}
            key={i}
          />
        );
      })}
    </Col>
  );
}

CommentView.propTypes = {
  comments: PropTypes.array,
};
