import React from "react";
import UserContext from "../UserContext";
import { Redirect } from "react-router-dom";

export default function Exit(props) {
  const { setUserContext } = React.useContext(UserContext);

  fetch("/api/exit").then((resp) => {
    if (resp.status === 200) setUserContext({ isAuthorized: false });
  });
  return <Redirect to="/" />;
}
