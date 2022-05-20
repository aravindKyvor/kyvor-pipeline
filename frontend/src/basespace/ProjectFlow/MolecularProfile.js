import React, { useEffect, useState } from "react";
import ReactSpeedometer from "react-d3-speedometer";

import { Card } from "react-bootstrap";
const MolecularProfile = () => {
  const [profile, setprofile] = useState([]);
  const [isLoading, setLoading] = useState(true);
  useEffect(() => {
    getprofile();
  }, []);

  let getprofile = async () => {
    let response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/get_molecular_profile/`
    );
    let res = await response.json();

    console.log(res);
    setprofile(res);
    setLoading(false);
  };
  return (
    <div>
      {profile.map((item, index) => {
        return (
          <div key={index}>
            <div style={{ display: "flex", justifyContent: "center" }}>
              <Card border="warning" style={{ width: "18rem" }}>
                <Card.Header style={{ textAlign: "center" }}>
                  <strong>{item.Profile}</strong>
                </Card.Header>
              </Card>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default MolecularProfile;
