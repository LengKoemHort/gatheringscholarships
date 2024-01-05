from rest_framework import serializers
from ScholarshipApp.models import Internationals,Locals

class InternationalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Internationals 
        fields=('InternationalId','InternationalName')

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Locals
        fields=('LocalId','LocalName')