from django.shortcuts import render

import csv

from rest_framework.decorators import api_view
from rest_framework.response import Response
class chif:
    def chiffrementcsv(self,file):
        dictionnaire=csv.DictReader(open(file+'.csv','r'))
        dict1 = [dict(ligne) for ligne in dictionnaire ] 
        return dict1
@api_view(['GET'])
def getfichier(request):
    file="publication/diabetes"
    rslt=chif()
    
    res=rslt.chiffrementcsv(file)
    return Response(res)
    

