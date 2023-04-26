from django.db import models



class FichierCsv(models.Model):
    fichier=models.FileField(upload_to="fichier")
    
    
