import React from "react";
import axios from "axios";




class ArticleDetail extends React.Component {
  state = {
    data: {}
  };

  componentDidMount() {
    
    axios.get(`${process.env.REACT_APP_API_URL}/api/get_project/`).then(res => {
      this.setState({
        data: res.data
        
      });
      console.log(this.setState({data:res.data}))
    });
   
  }

  
  render() {
   
        return (
            <div>
            
            </div>
          ) 
    
  }
}



export default ArticleDetail;