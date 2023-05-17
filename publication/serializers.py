from .models import *
from  rest_framework import serializers

class fileserial(serializers.ModelSerializer):
     class Meta:
        model=FichierCsv
        fields='__all__'



