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
        
        
        
class FDA_Serializer(serializers.ModelSerializer):
    class Meta:
        model= FDA_Sheets
        fields='__all__'


class ClinicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= Clinical_DATA
        fields='__all__'

class SNVDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=SNV_datas
        fields='__all__'



class INDELDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=INDEL_datas
        fields='__all__'