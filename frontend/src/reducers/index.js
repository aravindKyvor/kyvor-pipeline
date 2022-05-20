import { combineReducers } from 'redux';
import auth from './auth';
import biosample from './biosample';
import project from './project';
import analysis from './analysis';

export default combineReducers({
  
    auth,
   project,
   biosample,
   analysis,
 

  
});
