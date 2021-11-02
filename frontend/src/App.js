import React, { useEffect } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  // Link,
  // useRouteMatch,
  // useParams,
} from "react-router-dom";
import Container from "react-bootstrap/Container";

import FormView from "./formview/FormView";
import ContentView from "./contentview/ContentView";
import NavigationView from "./navbar/navigationview/NavigationView";
import Registration from "./navbar/Registration";
import Enter from "./navbar/Enter";
import { UserContext, anonymous } from "./UserContext";
import Exit from "./navbar/Exit";

export default function App() {
  const [user, setUser] = React.useState(anonymous);
  useEffect(() => {
    fetch("/api/check_user").then((resp) => {
      if (resp.status === 200) {
        setUser({ isAuthorized: true });
        console.log("Ok");
      }
    });
  }, []);

  return (
    <Router>
      <UserContext.Provider
        value={{
          userContext: user,
          setUserContext: (newUser) => {
            console.log("newUser", newUser);
            setUser(newUser);
          },
        }}
      >
        <NavigationView />
        <Container>
          <Switch>
            <Route path="/registration">
              <Registration />
            </Route>
            <Route path="/enter">
              <Enter />
            </Route>
            <Route path="/exit">
              <Exit />
            </Route>
            <Route path="/" exact>
              <ContentView />
              <FormView />
            </Route>
          </Switch>
        </Container>
      </UserContext.Provider>
    </Router>
  );
}
