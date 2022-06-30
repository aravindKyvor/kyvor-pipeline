import React from 'react'

const Print = ({handlePrint}) => {
  return (
    <div>
        <button onClick={handlePrint}>
           print
        </button>
    </div>
  )
}

export default Print