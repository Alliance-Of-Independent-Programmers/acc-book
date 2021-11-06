import React, { useEffect, useState } from "react";
// import OnlineView from "../contentview/onlineview/OnlineView";
// import FormView from "../formview/FormView";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import UserInfoView from "./UserInfoView";

export default function Profile(props) {
  const [data, setData] = useState([]);
  const login = window.location["pathname"].slice(1);
  const formSend = (event) => {
    const data = new FormData();
    data.append("login", login);
    fetch("/api/user_info_construct", {
      method: "POST",
      body: data,
    }).finally(() => document.location.reload());
    event.preventDefault();
  };

  const getData = async (url) => {
    const response = await fetch(url);

    return await response.json();
  };
  useEffect(() => {
    getData("/api/user_info_construct").then((data) => setData(data));
  }, []);

  return (
    <Row>
      <Form onSubmit={formSend}>
        <Button variant="primary" type="submit">
          Закоментить
        </Button>
      </Form>
      <Col>
        <h1>В онлайне</h1>
        <UserInfoView onlarr={data} />
      </Col>
    </Row>
  );
}
