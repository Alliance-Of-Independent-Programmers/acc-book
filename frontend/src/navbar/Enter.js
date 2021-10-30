import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

export default function Enter() {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const [data2, setData2] = useState("");

  const getData = async (url) => {
    const response = await fetch(url);

    return await response.json();
  };
  getData("/api/accepted_enter_jsonrespons").then((data2) => setData2(data2));
  console.log(data2);

  const formSend = (event) => {
    const data = new FormData();
    data.append("password", password);
    data.append("login", login);
    // data.append("img", img);

    fetch("/api/enter", {
      method: "POST",
      body: data,
    }).finally(() => document.location.reload());
    event.preventDefault();
  };

  return (
    <Form onSubmit={formSend}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control
          type="email"
          placeholder="Enter email"
          name="login"
          value={login}
          onChange={(event) => {
            setLogin(event.target.value);
          }}
        />
        <Form.Text className="text-muted">
          We will never share your email with anyone else.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          placeholder="Password"
          name="password"
          value={password}
          onChange={(event) => {
            setPassword(event.target.value);
          }}
        />
      </Form.Group>
      <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Check me out" />
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
}
