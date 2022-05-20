from rest_framework import serializers
from django import forms
from .models import *


class BasespaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basespace
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class BiosampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biosample
        fields = "__all__"

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisStatus
        fields = "__all__"
        
        
        
        
class PortalSerializer(serializers.ModelSerializer):
    class Meta: 
        model= PatientPortal
        fields='__all__'