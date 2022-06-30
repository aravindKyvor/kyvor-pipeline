import React,{useEffect,useState} from 'react'
import { Card ,Button,Alert} from 'react-bootstrap'
import '../../index.css'
const TMB = () => {
  const [TMB, setTMB] = useState([]);
  const[STATUS,setSTATUS]=useState([]);
  const [MSI, setMSI] = useState([]);
  const[MSI_STATUS,setMSI_STATUS] = useState([]);
  useEffect(() => {
    getTMB();
    getMSI()
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
    
  };
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
   
  };
  return (
    <div>
        <Card className="text-center uvs-curve" >

  <Card.Body>
    <Card.Title style={{fontFamily:"Cuprum"}}><h3 ><strong>CANLYTx® Findings</strong></h3></Card.Title>
    <Card.Text>
     <div>
     {[
   
    'dark',
  ].map((variant) => (
    <Alert key={variant} variant={variant}>
      <strong>TMB:</strong>{STATUS} ({TMB} Muts/Mb)     <br/>                  <strong>MSI:</strong>{MSI_STATUS} ({MSI})
    </Alert>
  ))}
     </div>

    <br/>
    <h5>TARGETABLE MUTATION DETECTED</h5>
     <div className="example1">
  <p>Molecular profile: EGFR (CN 68), CCND3 (CN 13), VEGFA (CN 12), AKT3 (CN 7), MCL1 (CN 6) and MYC (CN 7), TP53 D18Vfs*63 (VAF-0.795)</p>
     </div>
    </Card.Text>
   
  </Card.Body>
 
</Card>
    </div>
  )
}

export default TMB