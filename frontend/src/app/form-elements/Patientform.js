// import { addDATAS } from '../../actions/pipes';
// import { Form } from 'react-bootstrap';
// import PropTypes from "prop-types";
// import React, { Component } from "react";
// import { Link } from 'react-router-dom';
// import { connect } from "react-redux";
// function validate(projectName, biosampleTumorfile1,biosampleTumorfile2,biosampleTumorfile3,biosampleTumorfile4) {
  
//   const errors = [];

//   if (projectName.length === 0) {
//     errors.push("Name can't be empty");
//   }
  
//   biosampleTumorfile1 = String(biosampleTumorfile1).split(".txt")[0]
//   if(!String(biosampleTumorfile1).endsWith("fastq.gz")){
//     errors.push("Extension Error")
//   }
//   var splitFile1 = String(biosampleTumorfile1).split('.')[0].split('_')
//   if ((splitFile1.length) !== 5){
    
//     errors.push('1.Filename Issue')

//  }
//  else if(String(splitFile1[1])[0] !== "S"){
 
//   errors.push(' 2.Filename Issue')

// }
// else if(String(splitFile1[2])[0] !== "L"){
 
//   errors.push('3.Filename Issue')

// }
// else if(String(splitFile1[2]).length !== 4){
  
//   errors.push('4.Filename Issue')

// }
// else if(String(splitFile1[3])[0] !== "R"){
  
//   errors.push('5.Filename Issue')

// }
// else if(String(splitFile1[4]).length !== 3){
 
//   errors.push('6.Filename Issue')

// }




//     biosampleTumorfile2 = String(biosampleTumorfile2).split(".txt")[0]
//     if(!String(biosampleTumorfile2).endsWith("fastq.gz")){
//       errors.push("Extension Error")
//     }
//     var splitFile2 = String(biosampleTumorfile1).split('.')[0].split('_')
//     if ((splitFile2.length) !== 5){
      
//       errors.push('1.Filename Issue')

//     }
//     else if(String(splitFile2[1])[0] !== "S"){

//     errors.push(' 2.Filename Issue')

//     }
//     else if(String(splitFile2[2])[0] !== "L"){

//     errors.push('3.Filename Issue')

//     }
//     else if(String(splitFile2[2]).length !== 4){

//     errors.push('4.Filename Issue')

//     }
//     else if(String(splitFile2[3])[0] !== "R"){

//     errors.push('5.Filename Issue')

//     }
//     else if(String(splitFile2[4]).length !== 3){

//     errors.push('6.Filename Issue')

//     }
    


//     biosampleTumorfile3 = String(biosampleTumorfile3).split(".txt")[0]
//     if(!String(biosampleTumorfile3).endsWith("fastq.gz")){
//       errors.push("Extension Error")
//     }
//     var splitFile3 = String(biosampleTumorfile3).split('.')[0].split('_')
//     if ((splitFile3.length) !== 5){
      
//       errors.push('1.Filename Issue')

//     }
//     else if(String(splitFile3[1])[0] !== "S"){

//     errors.push(' 2.Filename Issue')

//     }
//     else if(String(splitFile3[2])[0] !== "L"){

//     errors.push('3.Filename Issue')

//     }
//     else if(String(splitFile3[2]).length !== 4){

//     errors.push('4.Filename Issue')

//     }
//     else if(String(splitFile3[3])[0] !== "R"){

//     errors.push('5.Filename Issue')

//     }
//     else if(String(splitFile3[4]).length !== 3){

//     errors.push('6.Filename Issue')

//     }




//     biosampleTumorfile4 = String(biosampleTumorfile4).split(".txt")[0]
//     if(!String(biosampleTumorfile4).endsWith("fastq.gz")){
//       errors.push("Extension Error")
//     }
//     var splitFile4 = String(biosampleTumorfile4).split('.')[0].split('_')
//     if ((splitFile4.length) !== 5){
      
//       errors.push('1.Filename Issue')

//     }
//     else if(String(splitFile4[1])[0] !== "S"){

//     errors.push(' 2.Filename Issue')

//     }
//     else if(String(splitFile4[2])[0] !== "L"){

//     errors.push('3.Filename Issue')

//     }
//     else if(String(splitFile4[2]).length !== 4){

//     errors.push('4.Filename Issue')

//     }
//     else if(String(splitFile4[3])[0] !== "R"){

//     errors.push('5.Filename Issue')

//     }
//     else if(String(splitFile4[4]).length !== 3){

//     errors.push('6.Filename Issue')

//     }


//     return errors





// }

// class AddProduct extends Component {
//   state = {
//     projectName: "",
//     cancerType: "",
//     biosampleTumorfile1: "",
//     biosampleTumorfile2: "",
//     biosampleTumorfile3: "",
//     biosampleTumorfile4: "",
//   };
//   static propTypes = {
//     addDATAS: PropTypes.func.isRequired,
//   };

//   onChange = (e) => this.setState({ [e.target.name]: e.target.value });

//   onSubmit = (e) => {
//     e.preventDefault();
//     const { projectName, biosampleTumorfile1,biosampleTumorfile2,biosampleTumorfile3,biosampleTumorfile4 } = this.state;
//     const project = { projectName, biosampleTumorfile1,biosampleTumorfile2,biosampleTumorfile3,biosampleTumorfile4};
//     const errors = validate(projectName, biosampleTumorfile1,biosampleTumorfile2,biosampleTumorfile3,biosampleTumorfile4);
//     if (errors.length > 0) {
//     this.setState({ errors });
//       return
    
//     }
//     this.props.addDATAS(project,errors);
//     this.setState({
//       projectName: "",
//       cancerType: "",
//       biosampleTumorfile1: "",
//       biosampleTumorfile2: "",
//       biosampleTumorfile3: "",
//       biosampleTumorfile4: "",
//     });
//   };

//   render() {
//     const { errors, projectName, biosampleTumorfile1,biosampleTumorfile2,biosampleTumorfile3,biosampleTumorfile4 } = this.state;
//     return (
//       <div>
//         <div className="page-header">
     
//           <h3 className="page-projectName"> Patient Form </h3> 
//           <nav aria-label="breadcrumb">
//             <ol className="breadcrumb">
//               <li className="breadcrumb-item"><a href="!#" onClick={event => event.preventDefault()}>Forms</a></li>
//               <li className="breadcrumb-item active" aria-current="page">Form elements</li>
//             </ol>
//           </nav>
//         </div>
     
      
     
//          <div className=" col-11 grid-margin stretch-card ">
        
//             <div className="card">
//               <div className="card-body">
              
             
//                 <form className="forms-sample" onSubmit={this.onSubmit}>
//                 {errors&&errors.map(error => (
//           <p  className="alert alert-danger" role="alert" key={error}>Error: {error}  </p>
//         ))}
//                   <Form.Group>
//                     <label htmlFor="exampleInputUsername1">Project Name</label>
//                     <Form.Control type="text" id="exampleInputUsername1" placeholder="project Name" size="lg" name="projectName" onChange={this.onChange}
//               value={projectName}
//               required/>
//                   </Form.Group>
//                   <Form.Group>
//                     <label htmlFor="exampleInputCancerType">Cancer Type</label>
                
//                           <select className="form-control" required>
//                             <option>------ NONE ------</option>
//                             <option>Well differentiated Lung Adenocarcinoma</option>
//                             <option>Uterine Leiomyosarcoma</option>
//                             <option>Urothelial Carcinoma</option>
//                             <option>Triple Negative Metastatic Breast Cancer</option>
//                             <option>Triple Negative Breast Cancer</option>
//                             <option>Thyroid Cancer</option>
//                             <option>Thymoma and Thymic Carcinoma</option>
//                             <option>Synovial Sarcoma</option>
//                             <option>Stomach Cancer</option>
//                             <option>Serous Adenocarcinoma Ovary</option>
//                             <option>Second Primary Ca Stomach (First Primary Ca Breast )</option>
//                             <option>Sebaceous Carcinoma</option>
//                             <option>Sarcoma</option>
//                             <option>Rhabdomyosarcoma</option>
//                             <option>Renal Carcinoma (RCC)</option>
//                             <option>Recurrent Synovial Sarcoma</option>
//                             <option>Recurrent Sacral Chordoma</option>
//                             <option>Recurrent Chordoma</option>
//                             <option>Recurrent Carcinoma Thyroid</option>
//                             <option>RECURRENT CARCINOMA STOMACH WITH LIVER METASTASIS</option>
//                             <option>Recurrent Carcinoma Right Lung</option>
//                             <option>Recurrent Carcinoma Ovary</option>
//                             <option>Recurrent Anaplastic Hemangiopericytoma</option>
//                             <option>Rectal Cancer</option>
//                             <option>Prostate Cancer</option>
//                             <option>Poorly Differentiated Metastatic  Lung carcinoma</option>
//                             <option>Poorly differentiated Leiomyosarcoma</option>
//                             <option>POORLY DIFFERENTIATED ADENOCARCINOMA OF THE COLON</option>
//                             <option>Pleomorphic Liposarcoma With Local Recurrence</option>
//                             <option>Penile Cancer</option>
//                             <option>Papillary Carcinoma Lung</option>
//                             <option>Pancreatic Cancer</option>
//                             <option>Pancreatic Adenocarcinoma</option>
//                             <option>Ovarian Cancer</option>
//                             <option>Osteosarcoma Left Ilium</option>
//                             <option>Oropharyngeal Cancer</option>
//                             <option>Non-Small Cell Lung Carcinoma</option>
//                             <option>Neuroendocrine Tumor Duodenum</option>
//                             <option>Myelodysplastic Syndrome</option>
//                             <option>MUCINOUS ADENOCARCINOMA RECTO SIGMOID COLON WITH LIVER METASTASES AND OMENTUM</option>
//                             <option>Mucinous Adenocarcinoma of Appendix</option>
//                             <option>Moderately differentiated Squamous carcinoma of Tongue</option>
//                             <option>Moderately Differentiated Adenocarcinoma Lung</option>
//                             <option>Moderately Differentiated  Carcinoma of Sigmoid and Rectum</option>
//                             <option>Metastatic Urothelial Carcinoma</option>
//                             <option>Metastatic Renal Cell Carcinoma</option>
//                             <option>Metastatic Pulmonary Adenocarcinoma</option>
//                             <option>Metastatic Pancreatic Adenocarcinoma</option>
//                             <option>Metastatic Lung Carcinoma</option>
//                             <option>Metastatic Lung Adenocarcinoma</option>
//                             <option>Metastatic Left Renal Cell Carcinoma</option>
//                             <option>Metastatic Large Cell Neuroendocrine Carcinoma</option>
//                             <option>Metastatic High Grade  Osteosarcoma</option>
//                             <option>Metastatic Ewings Sarcoma Left Humerus</option>
//                             <option>METASTATIC CARCINOMA OF LEFT BREAST</option>
//                             <option>METASTATIC CARCINOMA OF BREAST</option>
//                             <option>Metastatic Carcinoma Lung</option>
//                             <option>Metastatic Carcinoma Left Kidney</option>
//                             <option>Metastatic Carcinoma Glottis</option>
//                             <option>Metastatic Carcinoma Breast</option>
//                             <option>Metastatic Carcinoma  Colon</option>
//                             <option>Metastatic Bifrontal Leiomyosarcoma</option>
//                             <option>Metastatic Adenosquamous Carcinoma lung</option>
//                             <option>Metastatic Adenocarcinoma Stomach</option>
//                             <option>Metastatic Adenocarcinoma of Stomach</option>
//                           </select>
                       
//                   </Form.Group>
//                   <Form.Group>
//                   <label id='inputGroupFile01' >BioSample TumorFile 1</label>
//                  <input type="file" className="form-control" id="inputGroupFile01" required name='biosampleTumorfile1' onChange={this.onChange}
//               value={biosampleTumorfile1}/>
  

//                   </Form.Group>
//                   <Form.Group>
//                   <label id='inputGroupFile02' >BioSample TumorFile 2</label>
//                  <input type="file" className="form-control" id="inputGroupFile02" name='biosampleTumorfile2' required  onChange={this.onChange}
//               value={biosampleTumorfile2}/>
  
                                 

  
                    
//                   </Form.Group>
//                   <Form.Group>
//                   <label id='inputGroupFile03'>BioSample TumorFile 3</label>
//                  <input type="file" className="form-control" id="inputGroupFile03"  name='biosampleTumorfile3' required  onChange={this.onChange}
//               value={biosampleTumorfile3}/>
  


                    
//                   </Form.Group>
//                   <Form.Group>
//                   <label id='inputGroupFile04' >BioSample TumorFile 4</label>
//                  <input type="file" className="form-control" id="inputGroupFile04" name='biosampleTumorfile4' required  onChange={this.onChange}
//               value={biosampleTumorfile4}/>
  
                                  

                    
//                   </Form.Group>
                
                  
                
                 
//                   <div class="col text-center">
//                   <button type="submit" className="btn  btn-info mr-2 btn-sm"  >Submit</button>
                 
//                   </div>
//                 </form>
//                 <div class="border border-light p-3 mb-4">

//     <div class="text-center">
//     <span><Link to='/'><button className="btn btn-light btn-sm"> Cancel</button></Link></span>
//     </div>

//   </div>
               
         
//               </div>
//             </div>
          
          

          
//           </div>

//        </div>
      
//     );
//   }
// }

// export default connect(null, { addDATAS })(AddProduct);


import React,{useState,useEffect} from 'react'

const Patientform = () => {
    let [testdata, settestdata] = useState([]);
    const [isLoading, setLoading] = useState(true);
  
    useEffect(() => {
      setInterval(function () {
        gettestdata();
      }, 5000);
    }, []);
  
    let gettestdata = async () => {
      let response = await fetch(
        `${process.env.REACT_APP_API_URL}/api/project_latest/`
        
      );
      let res = await response.json();
  
      console.log(res);
      settestdata(res);
      setLoading(false);
    };
  return (
    <div>Patientform</div>
  )
}

export default Patientform