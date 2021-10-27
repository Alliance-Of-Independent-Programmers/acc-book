import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";

export default function FormView(props) {
  const [img, setImg] = useState("");
  const [login, setLogin] = useState("");
  const [text, setText] = useState("");

  const formSend = (event) => {
    const data = new FormData();
    data.append("text", text);
    data.append("login", login);
    data.append("img", img);
    fetch("/api/example/app", {
      method: "POST",
      body: data,
    }).finally(() => document.location.reload());
    event.preventDefault();
  };

  return (
    <Row>
      <Form onSubmit={formSend}>
        <Form.Group controlId="formFile" className="mb-3">
          <Form.Label>Выберите аватар</Form.Label>
          <Form.Control
            type="file"
            name="img"
            value={img}
            onChange={(event) => {
              setImg(event.target.value);
            }}
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
          <Form.Label>Логин</Form.Label>
          <Form.Control
            type="text"
            name="login"
            value={login}
            onChange={(event) => {
              setLogin(event.target.value);
            }}
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
          <Form.Label>Комментарий</Form.Label>
          <Form.Control
            as="textarea"
            rows={3}
            name="text"
            value={text}
            onChange={(event) => {
              setText(event.target.value);
            }}
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Закоментить
        </Button>
      </Form>
    </Row>
  );
}
