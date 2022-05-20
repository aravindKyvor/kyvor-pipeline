import { POST_PATIENT_DATA, POST_PATIENT_ERROR } from "../actions/types";

const initialState = {
  projects: [],
  error: null,
};

// eslint-disable-next-line import/no-anonymous-default-export
export default function (state=initialState, action) {
  switch (action.type) {
    case POST_PATIENT_DATA:
      return {
        ...state,
        projects: [...state.projects, action.payload],
      };
    case POST_PATIENT_ERROR:
      return {
        projects: [],
        error: action.payload,
      };

    default:
      return state;
  }
}
