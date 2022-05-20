from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Basespace)
admin.site.register(Project)
admin.site.register(PipelineTO)
admin.site.register(AnalysisStatus)
admin.site.register(PatientPortal)
