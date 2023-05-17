from django.shortcuts import render
from .serializers import fileserial
from .models import FichierCsv
from django.conf import settings
import csv
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
import pandas as pd
from rest_framework.response import Response
class chif:
    def chiffrementcsv(self,file):
        dictionnaire=csv.DictReader(open(file,'r'))
        dict1 = [dict(ligne) for ligne in dictionnaire ] 
        return dict1
@api_view(['GET'])
def getfichier(request):
    file="publication/diabetes"
    rslt=chif()
    
    res=rslt.chiffrementcsv(file)
    return Response(res)
    
@api_view(['GET'])
def get_fichierUploader(request,id):
    fichier=FichierCsv.objects.get(id=id)
    fichierseriial=fileserial(fichier)
    nom=fichier.fichier.path
    print(nom)
    ouver=chif()
    
    dt=ouver.chiffrementcsv(nom)
    dictr=[dt,nom]
    return  Response(dictr)
class uploandingCsvfile(CreateAPIView):
    queryset =FichierCsv.objects.all()
    serializer_class=fileserial
    permission_classes=(AllowAny,)