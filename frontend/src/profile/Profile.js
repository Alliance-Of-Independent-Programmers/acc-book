import React, { useEffect, useState } from "react";
import OnlineView from "../contentview/onlineview/OnlineView";

export default function Profile(props) {
  const [data, setData] = useState([]);

  const getData = async (url) => {
    const response = await fetch(url);

    return await response.json();
  };

  useEffect(() => {
    getData("/api/online_view").then((data) => setData(data));
  }, []);
  return <OnlineView onlarr={data} />;
}
