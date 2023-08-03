from .models import *
from  rest_framework import serializers

class fileserial(serializers.ModelSerializer):
     class Meta:
        model=FichierCsv
        fields='__all__'
class ContexteSerial(serializers.Serializer):       
       nom=serializers.CharField()
       email=serializers.CharField()
       total=serializers.CharField()
       mention=serializers.CharField()
       moyenne=serializers.CharField()
       nombreCredit=serializers.CharField()
       cours=serializers.ListField(child=serializers.DictField())
       def get_nom(self):
               return self.nom




