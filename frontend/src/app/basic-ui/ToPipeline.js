// import React from 'react';
// import { Link } from 'react-router-dom';
// import axios from 'axios';
// class ToPipeline extends React.Component{
//     constructor(){
//         super();
//         this.state={
//             data:[],
//             DataisLoaded: false
           
//         };
//     }



//     componentDidMount(){
//         axios.get(
//             `${process.env.REACT_APP_API_URL}/api/get-pipeline-to`,{
              
//                 headers: {'Content-Type': 'application/json' ,
//                 "X-CSRFToken": '{{csrf_token}}'
//              },

//             }
//             )
//                         .then((res) => res.json())
//                         .then((json) => {
//                             this.setState({
//                                 data: json,
//                                 DataisLoaded: true
//                             });
//                         })
       
//     }
   
//     // deleteData(id){
//     //     fetch('http://127.0.0.1:8000/employee/'+id+'/',{
//     //         method:'DELETE',
//     //         body:JSON.stringify(this.state),
//     //     })
//     //     .then(response=>response)
//     //     .then((data)=>{
//     //         if(data){
//     //             this.fetchData();
//     //         }
//     //     });
//     // }

//     render(){
//         const { DataisLoaded } = this.state;
//         if (!DataisLoaded) return <div>
//             <h1> Pleses wait some time.... </h1> </div> ;
//         return (
//             <div>
//                 Pipline Data
//             </div>
//         );
//     }
    
// }

// export default ToPipeline;








import React, { useState, useEffect } from "react";
import Table from "react-bootstrap/Table";
import { Link } from "react-router-dom";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

toast.configure();
const ToPipeline = () => {
  let [project, setproject] = useState([]);

  useEffect(() => {
    setInterval(function () {
      getproject();
    }, 90000);
    console.log(project)
  }, [project]);

  let getproject = async () => {
    let response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/pipeline-to`,{
          
            headers: {'Content-Type': 'application/json' ,
            "X-CSRFToken": '{{csrf_token}}'
         },

        }
        )
    let data = await response.json();

    let new_data = data;
    // console.log(data)
    console.log(new_data);
    setproject(new_data);
  };
  return (
    <div>
     wait for some time
    </div>
  );
};

export default ToPipeline;
