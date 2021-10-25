import React from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";

export default function FormView(props) {
  return (
    <Row>
      <Form method="post" action="/api/example/app">
        {/*<Form.Group controlId="formFile" className="mb-3">*/}
        {/*  <Form.Label>Выберите аватар</Form.Label>*/}
        {/*  <Form.Control type="file" />*/}
        {/*</Form.Group>*/}
        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
          <Form.Label>Почта</Form.Label>
          <Form.Control type="email" name="email" />
        </Form.Group>
        <Form.Group className="mb-3" controlId="exampleForm.ControlTextarea1">
          <Form.Label>Комментарий</Form.Label>
          <Form.Control as="textarea" rows={3} name="text" />
        </Form.Group>
        <Button variant="primary" type="submit">
          Закоментить
        </Button>
      </Form>
    </Row>
  );
}
