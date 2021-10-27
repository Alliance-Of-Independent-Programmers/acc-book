import CommentView from "./commentview/CommentView";
import OnlineView from "./onlineview/OnlineView";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import React, { useState, useEffect } from "react";

export default function ContentView(props) {
  const [data, setData] = useState([]);
  const [data1, setData1] = useState([]);

  const getData = async (url) => {
    const response = await fetch(url);

    return await response.json();
  };

  const getData1 = async (url) => {
    const response = await fetch(url);

    return await response.json();
  };

  useEffect(() => {
    getData("/api/online_view").then((data) => setData(data));
    getData1("/api/comment1_view").then((data) => setData1(data));
  }, []);

  return (
    <Row>
      {data.length > 0 ? (
        <>
          <Col>
            <h1>В онлайне</h1>
            <OnlineView onlarr={data} />
          </Col>
          <Col xs={9}>
            <CommentView comments={data1} />
          </Col>
        </>
      ) : (
        <b>Loading...</b>
      )}
    </Row>
  );
}
