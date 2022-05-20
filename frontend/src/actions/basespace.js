import axios from "axios";

import { GET_ANALYSIS, GET_BIOSAMPLE, GET_PROJECT ,POST_PATIENT_DATA,POST_PATIENT_ERROR} from "./types";
import { toast } from "react-toastify";

import "react-toastify/dist/ReactToastify.css";

toast.configure();

export const getAnalysis = () => async (dispatch) => {
  const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/analysis/`);

  dispatch({
    type: GET_ANALYSIS,
    payload: res.data,
  });
};

export const getBiosample = () => async (dispatch) => {
  const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/biosample/`);

  dispatch({
    type: GET_BIOSAMPLE,
    payload: res.data,
  });
};

export const getProject = () => async (dispatch) => {
  const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/projects/`);

  dispatch({
    type: GET_PROJECT,
    payload: res.data,
  });
};


export const addPatientdata =(project)=>async(dispatch)=>{
  try{
const res= await axios.post(`${process.env.REACT_APP_API_URL}/api/portal/`, project)
dispatch({
  type: POST_PATIENT_DATA,
  payload: res.data
});
  }catch(error){
    dispatch({
      type:POST_PATIENT_ERROR,
      payload: 
        error.response && error.response.data.message 
        ? error.response.data.message
        : error.message
      
    })

  }

}