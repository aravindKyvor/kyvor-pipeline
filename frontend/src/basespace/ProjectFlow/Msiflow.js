import React, { useEffect, useState } from "react";
import ReactSpeedometer from "react-d3-speedometer";

import { Card } from "react-bootstrap";
const Msiflow = () => {
  const [MSI, setMSI] = useState([]);
  const[MSI_STATUS,setMSI_STATUS] = useState([]);
  const [isLoading, setLoading] = useState(true);
  useEffect(() => {
    getMSI();
  }, []);

  let getMSI = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_msi/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();
    let msi= res.MSI
    let status= res.STATUS
    console.log(res);
    setMSI(msi);
    setMSI_STATUS(status)
    setLoading(false);
  };
  return (
    <div >
      
    
<br></br>
      <div style={{ display: "flex", justifyContent: "center" }}>
        <ReactSpeedometer
          maxSegmentLabels={0}
          minValue={0} //<---here
          maxValue={100}
          segments={2}
          value={MSI}
          shrink={false}
          width={307}
          height={250}
          segmentColors={["#FF4500", "#228B22"]}
          customSegmentStops={[0, 20, 100]}
          customSegmentLabels={[
            {
              text: "Low",
              position: "OUTSIDE",
              color: "black",
            },
            {
              text: "High",
              position: "OUTSIDE",
              color: "#474747",
            },
          ]}
          startColor={"#2E3440"}
          endColor={"#4C566A"}
          needleColor="#D8DEE9"
          textColor={"#000000"}
        />
      </div>

      <div style={{ display: "flex", justifyContent: "center" }}>
        <Card border="warning" style={{ width: "18rem" }}>
          <Card.Header> <strong>MSI Results : MSI ({MSI})</strong> </Card.Header>
          <Card.Header><strong>Status : {MSI_STATUS}</strong></Card.Header>
        </Card>
      </div>
    </div>
  );
};

export default Msiflow;
