import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";

export default function FormView(props) {
  const [text, setText] = useState("");

  const formSend = (event) => {
    const data = new FormData();
    data.append("text", text);
    fetch("/api/quote", {
      method: "POST",
      body: data,
    }).finally(() => document.location.reload());
    event.preventDefault();
  };

  return (
    <Row>
      <Form onSubmit={formSend}>
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
