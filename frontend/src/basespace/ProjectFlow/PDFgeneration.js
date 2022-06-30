import { AppBar } from '@material-ui/core'
import React, { Fragment } from 'react'
import './App.css'
import {PDFViewer} from '@react-pdf/renderer'

import FinalReports from './FinalReports'

const PDFgeneration = () => {
    return (
        <Fragment>

            <PDFViewer width="1000" height="600" className="app" >
           
            </PDFViewer>

        </Fragment>
    )
}

export default PDFgeneration

// import React from 'react'

// const PDFgeneration = () => {
//   return (
//     <div>PDFgeneration</div>
//   )
// }

// export default PDFgeneration