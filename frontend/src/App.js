import React from "react";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

import CommentView from "./commentview/CommentView";
import comments from "./commentview/data";
import OnlineView from "./onlineview/OnlineView";
import onlarr from "./onlineview/data";

export default function App() {
  return (
    <>
      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">Цитатник</Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="#features">1</Nav.Link>
              <Nav.Link href="#pricing">2</Nav.Link>
              <NavDropdown title="Dropdown" id="collasible-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                  Another action
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">
                  Something
                </NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">
                  Separated link
                </NavDropdown.Item>
              </NavDropdown>
            </Nav>
            <Nav>
              <Nav.Link href="#deets">Регистрация</Nav.Link>
              <Nav.Link href="#memes">Вход</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <Container>
        <Row>
          <Col>
            <h1>В онлайне</h1>
            <OnlineView onlarr={onlarr} />
          </Col>
          <Col xs={9}>
            <CommentView comments={comments} />
          </Col>
        </Row>
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
            <Form.Group
              className="mb-3"
              controlId="exampleForm.ControlTextarea1"
            >
              <Form.Label>Комментарий</Form.Label>
              <Form.Control as="textarea" rows={3} name="text" />
            </Form.Group>
            <Button variant="primary" type="submit">
              Закоментить
            </Button>
          </Form>
        </Row>
      </Container>
    </>
  );
}
