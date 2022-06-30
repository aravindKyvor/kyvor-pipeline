import React, { useEffect, useState } from "react";
import { Card } from "react-bootstrap";
import ReactSpeedometer from "react-d3-speedometer";

const Tmb = () => {
  const [TMB, setTMB] = useState([]);
  const[STATUS,setSTATUS]=useState([]);
  const [isLoading, setLoading] = useState(true);
  useEffect(() => {
    getTMB();
  }, []);

  let getTMB = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_tmb/`,
      {
        responseType: "blob",
      }
    );
    let res = await response.json();
    let tmb= res[0]
    let status= res[1]
    console.log(res);
    setTMB(tmb);
    setSTATUS(status)
    setLoading(false);
  };
  return (
    <div >
      
      <br></br>
      <div style={{ display: "flex", justifyContent: "center" }}>
      
        <ReactSpeedometer
          maxSegmentLabels={0}
          minValue={0} //<---here
          maxValue={50}
          segments={3}
          value={STATUS}
          width={307}
         height={250}
          segmentColors={["#FF0000", "#fec107", "#008000"]}
          customSegmentStops={[0, 6, 19.9, 50]}
          customSegmentLabels={[
            {
              text: "Low",
              position: "OUTSIDE",
              color: "black",
            },
            {
              text: "Mid",
              position: "OUTSIDE",
              color: "#474747",
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
          <Card.Header><strong>TMB Results : {STATUS} Mut/Mb</strong></Card.Header>
          <Card.Header><strong>Status : {TMB}</strong></Card.Header>
         
        </Card>
      </div>
     
    </div>
  );
};

export default Tmb;
