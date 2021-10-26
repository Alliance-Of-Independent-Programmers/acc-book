import React from "react";
import Online from "./Online";
import PropTypes from "prop-types";

export default function OnlineView(props) {
  return (
    <>
      {props.onlarr.map((online, i) => {
        return <Online author={online.author} key={i} />;
      })}
    </>
  );
}

OnlineView.propTypes = {
  onlarr: PropTypes.array,
};
