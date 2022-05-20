import React from "react";
import { Modal } from "react-bootstrap";
import "react-toastify/dist/ReactToastify.css";
import { Link } from "react-router-dom";
import { Tab, Tabs } from "react-bootstrap";
import { Table } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
// import Tnpipeline from "../../basespace/ProjectFlow/Tnpipeline";
import Tmb from "../../basespace/ProjectFlow/Tmb";
import Msiflow from "../../basespace/ProjectFlow/Msiflow";
import FdaAppproved from "../../basespace/ProjectFlow/FdaAppproved";
import ClinicalStudies from "../../basespace/ProjectFlow/ClinicalStudies";
import GenomicSummary from "../../basespace/ProjectFlow/GenomicSummary";
import Vus from "../../basespace/ProjectFlow/Vus";
import Patientportal from "../../basespace/ProjectFlow/Patientportal";
import MolecularProfile from "../../basespace/ProjectFlow/MolecularProfile";
import TestRun from "../../basespace/ProjectFlow/Testrun";
import VusResults from "../../basespace/ProjectFlow/VusResults";
const ReportsTable = (props) => {
  return (
    <div>
      <div className="page-header">
        <h3 className="page-title">
          <span className="page-title-icon bg-gradient-primary text-white mr-2">
            <i className="mdi mdi-information menu-icon"></i>
          </span>{" "}
          Reports{" "}
        </h3>
        <nav aria-label="breadcrumb">
          <ul className="breadcrumb">
            <li className="breadcrumb-data active" aria-current="page">
              <span></span>
              <h4
                class="item_right font_cuprum"
                style={{ opacity: "1", right: "0px" }}
              >
                CANLY
                <span style={{ color: "#fec107" }}>
                  T<small style={{ fontSize: " 20px" }}>x</small>
                </span>
                <span style={{ fontWeight: "normal" }}>™</span>
              </h4>
            </li>
          </ul>
        </nav>
      </div>
    <div>
      <Patientportal/>
    </div>

      <Tabs
        defaultActiveKey="BioMarkers"
        transition={false}
        id="noanim-tab-example"
        className="mb-0.7"
      >
        <Tab eventKey="BioMarkers" title="BioMarkers">
          <div class="card-deck">
            <div class="card mb-4">
              <div class="card-body">
                <h4 class="card-title">TMB</h4>
                <p class="card-text">
                  <Tmb />
                </p>
              </div>
            </div>
            <div class="card mb-4">
              <div class="card-body">
                <h4 class="card-title">MSI</h4>
                <p class="card-text">
                  <Msiflow />
                </p>
              </div>
            </div>
            <div class="card mb-4">
              <div class="card-body">
                <h4 class="card-title">GenomicProfile</h4>
                <br></br>

                <MolecularProfile />
              </div>
            </div>
          </div>
        </Tab>
        <br></br>
        <Tab eventKey="FDA/NCCN-Approved" title="FDA/NCCN -Approved">
          <FdaAppproved />
        </Tab>
        <br></br>

        <Tab eventKey="GenomicSummary" title="Genomic Summary">
          <GenomicSummary />
        </Tab>
        <br></br>
        <Tab eventKey="Clinicaltrials" title="Clinical Trials">
          <ClinicalStudies />
        </Tab>
        <br></br>

        <Tab eventKey="Clinical/casestudeis" title="Clinical/casestudeis">
          <p>Clinical/casestudeis</p>
        </Tab>
        <br></br>
        <Tab eventKey="PGxFDAlabel" title="PGxFDA label">
          {/* <Tnpipeline /> */}
          <Vus />
        </Tab>
        <br></br>
        <Tab eventKey="VUS" title=" VUS">
         <VusResults/>
        </Tab>
      </Tabs>
    </div>
  );
};

export default ReportsTable;
