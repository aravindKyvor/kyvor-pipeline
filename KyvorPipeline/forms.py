from django import forms
from .models import *

project_type_choices = (
    (1, "TO"),
    (2, "TN"),
    (3, "NO")
)


class PipelineToForm(forms.Form):
    project_name = forms.CharField(label="Project Name", max_length=120)
    project_type = forms.ChoiceField(label="Project Type", choices=project_type_choices)
    project_rerun = forms.BooleanField(label="Rerun - Yes or No")
    project_cancer_type = forms.CharField(label="Cancer Types (comma seperated)", max_length=240)
    biosample_folder = forms.URLField(label="Mention Biosample Path", max_length=360)


