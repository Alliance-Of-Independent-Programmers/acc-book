import React from "react";
import Online from "./Online";
import PropTypes from "prop-types";

export default function OnlineView(props) {
  return (
    <>
      {props.onlarr.map((online, i) => {
        return <Online img={online.img} login={online.login} key={i} />;
      })}
    </>
  );
}

OnlineView.propTypes = {
  onlarr: PropTypes.array,
};
