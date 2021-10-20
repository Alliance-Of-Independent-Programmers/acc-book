import React from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";

export default function App() {
  return (
    <Container>
      <h1>Привет, мир!</h1>
      <Button onClick={() => console.log("Hello")} variant="warning">
        Warning
      </Button>
    </Container>
  );
}
