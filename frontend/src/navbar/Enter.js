import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import UserContext from "../UserContext";
import { Redirect } from "react-router-dom";

export default function Enter() {
  const { userContext, setUserContext } = React.useContext(UserContext);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const formSend = (event) => {
    const data = new FormData();
    data.append("password", password);
    data.append("email", email);
    // data.append("img", img);

    fetch("/api/enter", {
      method: "POST",
      body: data,
    })
      .then((resp) => {
        if (resp.status === 200) {
          setUserContext({ isAuthorized: true });
          console.log("Ok");
        } else {
          console.log("Логин или пароль не верны");
        }
      })
      .catch((err) => {
        document.location.reload();
        console.error(err);
      });
    event.preventDefault();
  };
  if (userContext.isAuthorized) return <Redirect to="/" />;
  else
    return (
      <Form onSubmit={formSend}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter email"
            name="email"
            value={email}
            onChange={(event) => {
              setEmail(event.target.value);
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
