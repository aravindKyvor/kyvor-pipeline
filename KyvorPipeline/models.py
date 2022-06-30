from django.db import models
from datetime import datetime
import uuid

# Create your models here.
class Basespace(models.Model):
    bs_email = models.EmailField(null=False, blank=False)
    bs_pwd = models.CharField(max_length=50, blank=False, null=False)
    bs_access_token = models.CharField(max_length=120, blank=False, null=False)
    bs_user_id = models.CharField(max_length=20, blank=False, null=False)
    novogene_bed_id = models.CharField(max_length=20, blank=False, null=False)
    novogene_gcc_id = models.CharField(max_length=20, blank=False, null=False)
    fulgent_bed_id = models.CharField(max_length=20, blank=False, null=False)
    fulgent_gcc_id = models.CharField(max_length=20, blank=False, null=False)
    bs_date_created = models.DateTimeField(auto_now_add=True)
    bs_expiry_on = models.DateTimeField(null=True)
    bs_credits = models.IntegerField(null=True)
    bs_active = models.BooleanField(default=True)

    def __str__(self):
        return "ID: %s, Email: %s" % (self.id, self.bs_email)


class Project(models.Model):
    bs_user_id = models.ForeignKey(Basespace, on_delete=models.PROTECT, null=False)
    project_name = models.CharField(max_length=40, blank=False, null=False)
    bs_default_project = models.CharField(max_length=40, blank=False, null=False)
    bs_project_id = models.CharField(max_length=40, blank=False, null=False)
    project_type = models.CharField(max_length=40, blank=False, null=False)
    project_created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
            get_latest_by = ['project_name']
   

    def __str__(self):
        return "ID: %s, ProjectName: %s"%(self.id, self.project_name)


class Biosample(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT, null=False)
    biosample_id = models.CharField(max_length=40, blank=False, null=True)
    biosample_type = models.CharField(max_length=20, blank=False, null=True)
    biosample_name = models.CharField(max_length=120, blank=False, null=True)
    biosample_path = models.CharField(max_length=480, blank=False, null=True)
    library_id = models.CharField(max_length=40, blank=False, null=True)
    biosample_created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "ID: %s, BiosampleName: %s" % (self.id, self.biosample_name)


class PipelineTO(models.Model):
    project_name = models.CharField(max_length=120, null=False, blank=False)
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True, null=True)
    biosample_t_file1 = models.FileField(Project, blank=False, null=False)
    biosample_t_file2 = models.FileField(Project, blank=False, null=False)
    biosample_t_file3 = models.FileField(Project, blank=False, null=False)
    biosample_t_file4 = models.FileField(Project, blank=False, null=False)
    biosample_to_id = models.ForeignKey(Biosample, on_delete=models.PROTECT, null=False)
    project_cancer_type = models.CharField(max_length=120, null=False)
    pipeline_initiated_on = models.DateTimeField(auto_now_add=True)
    pipeline_finished_on = models.DateTimeField(blank=True)
    pipeline_status = models.CharField(blank=True, max_length=120)

class AnalysisStatus(models.Model):
    analysis_type = models.CharField(max_length=120, blank=False, null=False)
    analysis_ref_id = models.CharField(max_length=20, blank=False, null=False)
    analysis_status = models.CharField(max_length=120, blank=False, null=False)
    analysis_description = models.TextField(blank=True, null=True)
    analysis_timestamp = models.DateTimeField(auto_now_add=True)
    bs_analysis_id = models.CharField(max_length=120, blank=True, null=True)
    bs_analysis_status = models.CharField(max_length=120, blank=True, null=True)
    bs_analysis_name = models.CharField(max_length=120, blank=True, null=True)
    
    
    
    
    
class PatientPortal(models.Model):
    Patient_information=  models.CharField(max_length=500, blank=False, null=False)
    Physician_information=models.CharField(max_length=500, blank=False, null=False)
    Report_Date= models.DateTimeField(auto_now_add=True)
    Cancer_Type= models.CharField(max_length=500, blank=False, null=False)
    Specimen= models.CharField(max_length=880, blank=False, null=False)








class FDAReports(models.Model):
    Genes = models.CharField(max_length= 100)
    variants = models.CharField(max_length= 200)
    cancer_types = models.CharField(max_length= 500)
    
    
    
    
    
    
class FDA_Sheets(models.Model):
        id= models.IntegerField(primary_key=True,null=False, blank=False)
        GENE = models.CharField(max_length=200,null=True, blank=True)
        BIOMARKER=models.CharField(max_length=200,null=True, blank=True)
        VARIANT_CDS=models.CharField(max_length=200,null=True, blank=True)
        THERAPY=models.TextField()
        EVIDENCE_STATEMENT_1=models.TextField()
        EVIDENCE_STATEMENT_2=models.TextField()
        Status=models.CharField(max_length=200,null=True, blank=True)
        AF_VAF=models.CharField(max_length=200,null=True, blank=True)
        CANCER_TYPES=models.CharField(max_length=800,null=True, blank=True)
        
        
        
class Clinical_DATA(models.Model):
    id= models.IntegerField(primary_key=True,null=False, blank=False)
    nct_id=models.CharField(max_length=200,null=True, blank=True)
    official_title=models.TextField()
    intervention=models.TextField()
    variant_found=models.CharField(max_length=200,null=True, blank=True)
    url=models.URLField(max_length=2000,null=True, blank=True)
    BioMarker=models.CharField(max_length=200,null=True, blank=True)
    
    Reference=models.TextField()
    GENE=models.CharField(max_length=200,null=True, blank=True)
    
    VARIANT=models.CharField(max_length=200,null=True, blank=True)
    VARIANT_CDS=models.CharField(max_length=200,null=True, blank=True)
    THERAPY=models.TextField()
    EVIDENCE_STATEMENT_1=models.TextField()
    EVIDENCE_STATEMENT_2=models.TextField()
    Status=models.CharField(max_length=200,null=True, blank=True)
    AF_VAF=models.CharField(max_length=200,null=True, blank=True)
    
    CANCER_TYPES=models.CharField(max_length=200,null=True, blank=True)
    
    
    

class SNV_datas(models.Model):
    id= models.IntegerField(primary_key=True,null=False, blank=False)
    GENE=models.CharField(max_length=400,null=True, blank=True)
    AMINO_ACID_CHANGE=models.CharField(max_length=500,null=True, blank=True)
    CDS=models.CharField(max_length=500,null=True, blank=True)




class INDEL_datas(models.Model):
    id= models.IntegerField(primary_key=True,null=False, blank=False)
    GENE=models.CharField(max_length=400,null=True, blank=True)
    AMINO_ACID_CHANGE=models.CharField(max_length=500,null=True, blank=True)
    CDS=models.CharField(max_length=500,null=True, blank=True)