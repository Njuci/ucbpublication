from django.shortcuts import render
from .serializers import fileserial
from .models import FichierCsv
from django.conf import settings
import csv
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .email_sending import envoi_email
from datetime import datetime
class chif:
    def chiffrementcsv(self,file):
        dictionnaire=csv.DictReader(open(file,'r'))
        dict1 = [dict(ligne) for ligne in dictionnaire ] 
        print(dict1)
        return dict1
def chiffrementrafine(c):
    f=[]
    for i in range(len(c)):
        dictio={}           
        dictio['nom']=c[i].get('nom')
        dictio['email']=c[i].get('email')
        dictio['total']=c[i].get('total')
        dictio['mention']=c[i].get('mention')
        dictio['moyenne']=c[i].get('moyenne')
        dictio['nombreCredit']=c[i].get('nombreCredit')
        cours=[]
        for a in c[i].keys():
            if a  in dictio.keys():
                print('')
            else:
                print(a)
                fg={}
                fg[a]=c[i].get(a)
                cours.append(fg)
        dictio['cours']=cours
        f.append(dictio)
    return f
from rest_framework.views import APIView

class MyView(APIView):
    def post(self, request):
        serializer = fileserial(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            rslt=chif()    
            file=instance.fichier.path
            res=rslt.chiffrementcsv(file)
            
            return Response(res)
        else:
            return Response(serializer.errors)
@api_view(['GET'])
def getfichier(request):
    file="publication/diabetes.csv"
    rslt=chif()
    
    res=rslt.chiffrementcsv(file)
    a=chiffrementrafine(res)
    return Response(a)
    
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
    def post(self, request):
        serializer = fileserial(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            rslt=chif()    
            file=instance.fichier.path
            res=rslt.chiffrementcsv(file)
            a=chiffrementrafine(res)
        
            return Response(a)
        else:
            return Response(serializer.errors)
@api_view(['POST'])
def Email_envoie(request, email,*args, **kwargs):
    """ This view help to create and account for testing sending mails."""
    cxt = {}
    if request.method == "POST":
        email = email

        subjet = "Test Email"
        template = 'email.html'
        context = {
            'date': datetime.today().date,
            'email': email
        }

        receivers = [email]

        has_send = envoi_email(
            sujet=subjet,
            desti=receivers,
            template=template,
            context=context
            )

        if has_send:
           cxt =  {"msg":"mail envoyee avec success."}
        else:
            cxt = {'msg':'email envoie echoue.'}
        print(has_send)

    return Response(cxt,status=status.HTTP_200_OK)       