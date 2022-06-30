// import * as React from 'react';
// import Box from '@mui/material/Box';
// import Paper from '@mui/material/Paper';
// import Stack from '@mui/material/Stack';
// import { styled } from '@mui/material/styles';
import logo1 from './kyvor_logo.png'
import logo2 from './cantylx.png'
// import { Navbar, Container } from 'react-bootstrap';

// const BasicStack = () => {
//   return (
//     <div>
//       <Navbar>

//         <Navbar.Brand >
//           <img width="150%" src={logo1} />

//         </Navbar.Brand>
//         <Navbar.Toggle />
//         <Navbar.Collapse className="justify-content-end">
//           <Navbar.Text>
//             <img width="100%" src={logo2} />
//           </Navbar.Text>
//         </Navbar.Collapse>

//       </Navbar>
//     </div>



//   );
// }

// export default BasicStack;

import React from 'react';
import '../../index.css'
import {
  MDBNavbar,
  MDBNavbarNav,
  MDBNavbarItem,
  MDBNavbarLink,
  MDBNavbarToggler,
  MDBContainer,
  MDBIcon
} from 'mdb-react-ui-kit';

function BasicStack() {
  return (
    <header>
     

      <div style={{display: 'flex'}} >
        <div>
        <img width="22%" src={logo1} style={{marginBottom:'-10%'}}/>
        </div>
        <div >
        <img width="110%" src={logo2} style={{marginLeft:'auto',marginTop:'30%'}}/>
        </div>
      
     </div>
    </header>
  );
}

export default BasicStack