from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Basespace)
admin.site.register(Project)
admin.site.register(PipelineTO)
admin.site.register(AnalysisStatus)
admin.site.register(PatientPortal)
admin.site.register(FDAReports)

admin.site.register(FDA_Sheets)
admin.site.register(Clinical_DATA)
admin.site.register(SNV_datas)
admin.site.register(INDEL_datas)