import React from "react";
import Container from "react-bootstrap/Container";

import FormView from "./formview/FormView";
import ContentView from "./contentview/ContentView";
import NavigationView from "./navigationview/NavigationView";

export default function App() {
  return (
    <>
      <NavigationView />
      <Container>
        <ContentView />
        <FormView />
      </Container>
    </>
  );
}
