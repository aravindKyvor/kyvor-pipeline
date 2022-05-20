import { GET_ANALYSIS } from "../actions/types";

const initialState = {
  analysis: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_ANALYSIS:
      return {
        ...state,
        analysis: action.payload,
      };

   
    default:
      return state;
  }
}
