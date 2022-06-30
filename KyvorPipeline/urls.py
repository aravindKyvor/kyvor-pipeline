from django.urls import include, path
from rest_framework import routers
from . import views
from .pipelinesupport.annotsv import RunAnnotsv
from .pipelinesupport.annovar import RunAnnovar
from .pipelinesupport.basespace import usercreds
from .pipelinesupport.basespace import CreateProject
from .pipelinesupport.basespace import CreateBioSample
from .pipelinesupport.basespace import LaunchDSP
from .pipelinesupport.basespace import LaunchDE
from .pipelinesupport.clinicaltrials import clinicalLauncher
from .pipelinesupport.CurationV3 import curation
from .pipelinesupport.DE import CurationDE
from .pipelinesupport.DSP import CurationDSP
from .pipelinesupport.ichorCNA import RunIchorCNA
from .pipelinesupport.msisensor import RunMsiSensorTO

from django.views.decorators.csrf import csrf_exempt
router = routers.DefaultRouter()
router.register(r'basespace', views.BasespaceViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'biosamples', views.BiosampleViewSet)
router.register(r'analysis', views.AnalysisViewSet)
router.register(r'portal', views.Patient_Portal)
router.register(r'fda',views.FDA_DATABASE)
router.register(r'clinicaldata',views.ClinicalDatabases)
router.register(r'snv_database',views.SNVdatabase)
router.register(r'indel_database',views.INDELdatabase)

urlpatterns = [
    path('', include(router.urls)),
    path('pipeline-to', views.PipelineTO.as_view(), name='pipeline-to'),

    path('pipeline-tn', views.PipelineTN.as_view(), name='pipeline-tn'),

    path('annotsv', views.RunAnnotsv, name='annotsv'),
    path('annovar', views.RunAnnovar, name='annovar'),
    path('RunIchorCNA', views.RunIchorCNA, name='RunIchorCNA'),

    path('CreateBioSample', views.CreateBioSample, name='createbiosample'),
    path('LaunchDSP', views.LaunchDSP, name='launchDSP'),
    path('LaunchDE', views.LaunchDE, name='launchDE'),
    path('clinicalLauncher', views.clinicalLauncher, name='clinicalLauncher'),
    path('curation', views.curation, name='curation'),
    path('CurationDE', views.CurationDE, name='CurationDE'),
    path('CurationDSP', views.CurationDSP, name='CurationDSP'),
    path('RunIchorCNA', views.RunIchorCNA, name='RunIchorCNA'),
    path('RunMsiSensorTO', views.RunMsiSensorTO, name='RunMsiSensorTO'),
    path('analysis/', views.get_analysis),
    path('applications/', views.get_application),
    path('users/', views.get_user),
    path('credits/', views.get_credits),
    path('get_files/', views.get_files),
    path('get_annovar/', views.get_Annovar_data),
    path('get_dsp/', views.get_DSP_data),
    path('get_biosamples/', views.get_Biosamples),
    path('analysis_latest/', views.analysis_latest),
    path('get_DE/', views.get_DE_data),
    path('get_clinicaltrails/', views.get_clinicalTrails),
    path('get_clinicalstudies/', views.get_clinicalStudies),
    path('get_latest_project/', views.get_latest_project),
    path('get_status/', views.get_status_on_data_uploading),
    path('get_whoami/', views.get_whoami),
    path('get_tmb/', views.get_TMBvalues),
    path('get_msi/', views.MSI_values),
    path('get_tests/', views.get_tests),
    path('get_vus/', views.get_VUS),
    path('get_results/', views.results),
    path('get_biosampleid/', views.get_biosampleId),
   
    path('get_clilical_data/', views.clinicaldata),
    path('get_fda/', views.get_fdaValues),
    path('get_clinicalreport/', views.get_clilicalReport),
    path('get_molecular_profile/', views.get_mocular_profile),
    
    
    #----------------------get_patient_portal---------------------------#
    path('processed_file/', views.process_clilical_files),
    path('fda_filtered_sheets/', views.fad_sheet_filters),
    path('vus_results/',views.vus_results),
    path('genes_variants/',views.Genes_Variants_Cancertypes),
    path('de_results/',views.de_results),
    path('dsp_results/',views.DSP_results),
    path('patient_ids/',views.patient_ids),
    path('fda_database_results/',views.FDA_automated_results)

    

    



]
