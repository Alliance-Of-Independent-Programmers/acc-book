import React from "react";
import PropTypes from "prop-types";
import Col from "react-bootstrap/Col";
import Comment from "../contentview/commentview/Comment";
// import UserInfo from "./UserInfo";

export default function UserQuotsView(props) {
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

UserQuotsView.propTypes = {
  comments: PropTypes.array,
};
