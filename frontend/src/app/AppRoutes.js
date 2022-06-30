import React, { Component, Suspense, lazy } from "react";
import { Switch, Route, Redirect } from "react-router-dom";
import Projectform from "./Projectform";
import ReportsTable from "./basic-ui/ReportsTable";
import Spinner from "../app/shared/Spinner";
import Annovar from "./basic-ui/Annovar";
import Reports1 from "./basic-ui/Reports1";
import Basespace from "./basic-ui/Basespace";
import Basespace1 from "./basic-ui/Basespace1";
import Analysis2 from "./basic-ui/Analysis2";
import EditForm from "./form-elements/EditForm";
import Biosample from "../basespace/biosample/Biosample";
import ProjectList from "../basespace/projects/Projectlist";
import ApplicationList from "../basespace/applications/Applicationlist";
import ApplicationDetail from "../basespace/applications/ApplicationDetail";
import WhoAmI from "../basespace/users/WhoAmI";
import Credits from "../basespace/credits/Credits";
import AnalysisList from "../basespace/analysis/AnalysisList";
import Analysis from "./basic-ui/Analysis";
import PrivateRoute from "../PrivateRoutes";
import Google from "./user-pages/Google";
import Login from "./user-pages/Login";
import Dashboard from "./dashboard/Dashboard";
import Profile from "../app/shared/Profile";
import BasicElements from "./form-elements/BasicElements";
import MsiSensor from "../app/basic-ui/MsiSensor";
import AnnovarRun from "./basic-ui/AnnovarRun";
import DEcuration from "../app/basic-ui/DEcuration";
import DSPcuration from "../app/basic-ui/DSPcuration";
import AnnotSV from "./basic-ui/AnnotSv";
import ToPipeline from "./basic-ui/ToPipeline";
import Error404 from "./error-pages/Error404";
import Error500 from "./error-pages/Error500";
import Patientform from "./form-elements/Patientform";
import DE_OUTPUT from "./basic-ui/DEOutput";
import CNVkit from "./basic-ui/CNVkit";
import IchorCNA from "./basic-ui/IchorCNA";
import PdfIchor from "./basic-ui/PdfIchor";
import DECnv from "./basic-ui/DECNV";
import DEsv from "./basic-ui/DESV";
import ClinicalTrails from "./basic-ui/ClinicalTrails";
import ClinicalStudies from "./basic-ui/ClinicalStudeis";
import NewProject from "../basespace/projects/Newproject";
import ArticleDetail from "../basespace/analysis/AnalysisDetail";
import BsWhoAmi from "../basespace/ProjectFlow/Bswhoami";
import TNProjectForm from "./TnProjectForm";
import AnalysisForm from "./dashboard/AnalysisTO&TN";
import Tnpipeline from "../basespace/ProjectFlow/Tnpipeline";
import Vus from "../basespace/ProjectFlow/Vus";
import Patient_add_form from "../basespace/ProjectFlow/Patient_add_form";
import DeResults from "../basespace/ProjectFlow/DeResults";
import DspResults from "../basespace/ProjectFlow/DspResults";
// import FinalReports from "../basespace/ProjectFlow/FinalReports";
// import PDFgeneration from "../basespace/ProjectFlow/PDFgeneration";
import PDFGENE from '../basespace/PdfGeneration/PDFGENE'
class AppPrivateRoutes extends Component {
  render() {
    return (
      <Suspense fallback={<Spinner />}>
        <Switch>
          {/* Dashboard Starts  */}

          <PrivateRoute exact path="/" component={Dashboard} />
          <PrivateRoute
            exact
            path="/basespace/ToPipeline"
            component={ToPipeline}
          />

          <PrivateRoute
            path="/basic-ui/analysisform"
            component={AnalysisForm}
          />
          {/* Dashboard Ends */}

          {/* Basic ui Starts */}
          <PrivateRoute exact path="/basic-ui/Analysis" component={Analysis} />
          <PrivateRoute
            exact
            path="/basic-ui/Analysis2"
            component={Analysis2}
          />
          <PrivateRoute
            exact
            path="/basic-ui/reports"
            component={ReportsTable}
          />

          <PrivateRoute
            exact
            path="/basic-ui/Basespace1"
            component={Basespace1}
          />
          <PrivateRoute
            exact
            path="/basic-ui/Basespace"
            component={Basespace}
          />
          <PrivateRoute exact path="/basic-ui/Reports1" component={Reports1} />

          <PrivateRoute path="/basic-ui/Annovar" component={Annovar} />
          <PrivateRoute path="/basic-ui/AnnovarRun" component={AnnovarRun} />
          <PrivateRoute path="/basic-ui/Msisensor" component={MsiSensor} />
          <PrivateRoute path="/basic-ui/DEcuration" component={DEcuration} />
          <PrivateRoute path="/basic-ui/DSPcuration" component={DSPcuration} />
          <PrivateRoute path="/basic-ui/AnnotSV" component={AnnotSV} />
          <PrivateRoute path="/basic-ui/de/outputs" component={DE_OUTPUT} />
          <PrivateRoute path="/basic-ui/cnv" component={CNVkit} />
          <PrivateRoute path="/basic-ui/ichorCNA" component={IchorCNA} />
          <PrivateRoute path="/basic-ui/pdfichor" component={PdfIchor} />
          <PrivateRoute path="/basic-ui/DEcnv" component={DECnv} />
          <PrivateRoute path="/basic-ui/DEsv" component={DEsv} />
          <PrivateRoute path="/projectflow/vus" component={Vus} />
          <PrivateRoute
            path="/basic-ui/clinicalTrails"
            component={ClinicalTrails}
          />
          <PrivateRoute
            path="/basic-ui/clinicalstudies"
            component={ClinicalStudies}
          />
          <PrivateRoute path="/basic-ui/newproject" component={NewProject} />
          <PrivateRoute path="/basic-ui/analysi" component={ArticleDetail} />
          <PrivateRoute
            path="/basic-ui/patient/form"
            component={Patient_add_form}
          />

          <PrivateRoute path="/projectflow/DeResults" component={DeResults} />

          <PrivateRoute path="/projectflow/DspResults" component={DspResults} />
          <PrivateRoute path="/projectflow/finalReports" component={PDFGENE} />

          {/* Basic ui Ends */}

          {/* Shared Section Starts */}
          {/* Shared Section Ends */}

          {/* Basespace Biosample Section */}
          <PrivateRoute
            exact
            path="/basespace/biosample"
            component={Biosample}
          />

          {/* BaseSpace BioSample Ends */}

          {/*  BaseSpace Project Section */}
          <PrivateRoute
            exact
            path="/basespace/projects/list"
            component={ProjectList}
          />

          {/* Project Ends */}

          {/* Analysis secion */}

          <PrivateRoute
            exact
            path="/basespace/analysis/"
            component={AnalysisList}
          />
          {/* <PrivateRoute exact path ='/basespace/analysis/analysisdetail/:dataID/' component={ApplicationList}/> */}

          {/* Analysis End */}

          {/* Basespace Application Section */}

          <PrivateRoute
            exact
            path="/basespace/applicationlist"
            component={ApplicationList}
          />
          <PrivateRoute exact path="/view/:id" component={ApplicationDetail} />
          {/* Basespace Application Ends */}

          {/* Basespace User Section */}
          <PrivateRoute
            exact
            path="/basespace/users/whoami"
            component={WhoAmI}
          />
          {/* Basespace User Ends */}

          <PrivateRoute
            exact
            path="/form-Elements/basic-elements"
            component={BasicElements}
          />
          <PrivateRoute
            exact
            path="/form-Elements/patientform"
            component={Patientform}
          />
          <PrivateRoute
            exact
            path="/analysis/projectform"
            component={Projectform}
          />

          <PrivateRoute
            exact
            path="/analysis/tnprojectform"
            component={TNProjectForm}
          />
          <PrivateRoute
            exact
            path="/projectflow/bswhoami"
            component={Projectform}
          />
          <PrivateRoute
            exact
            path="/basespace/pipelineresults"
            component={Tnpipeline}
          />

          <PrivateRoute exact path="/basespace/credits" component={Credits} />

          <Route exact path="/user-pages/login-1" component={Login} />
          <Route exact path="/google" component={Google} />

          <PrivateRoute exact path="/update/:id" component={EditForm} />
          <Route path="*" exact={true} component={Error404} />

          <PrivateRoute
            exact
            path="/error-pages/error-500"
            component={Error500}
          />

          <PrivateRoute path="/profile" component={Profile} />
        </Switch>
      </Suspense>
    );
  }
}

export default AppPrivateRoutes;
