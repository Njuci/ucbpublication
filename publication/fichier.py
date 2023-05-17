


from django.shortcuts import render

from publication.models import FichierCsv

from django.conf import settings
import csv

fichier=FichierCsv.objects.get(id=1)

nom=fichier.get_fichier_nom()



print(nom)