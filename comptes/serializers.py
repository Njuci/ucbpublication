from rest_framework.serializers import ModelSerializer
from .models import *


#user serializer

class UtilisateurSerial(ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
class InstitutionSerial(ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
