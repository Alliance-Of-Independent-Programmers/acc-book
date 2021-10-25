import CommentView from "./commentview/CommentView";
import OnlineView from "./onlineview/OnlineView";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import React, { useState, useEffect } from "react";

export default function ContentView(props) {
  const [data, setData] = useState([]);

  const getResourse = async (url) => {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(
        "Ошибка по адресу ${url}, статус ошибки ${response.status}"
      );
    }
    return await response.json();
  };

  useEffect(() => {
    getResourse("/api/online_view").then((data) => setData(data));
  }, []);

  //
  // GetResourse("/api/online_view").then((data) => console.log(data[0]));
  return (
    <Row>
      {data.length > 0 ? (
        <>
          <Col>
            <h1>В онлайне</h1>
            <OnlineView onlarr={data} />
          </Col>
          <Col xs={9}>
            <CommentView comments={data} />
          </Col>
        </>
      ) : (
        <b>Loading...</b>
      )}
    </Row>
  );
}
