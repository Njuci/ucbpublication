from django.db import models



class FichierCsv(models.Model):
    nom=models.CharField(max_length=80,unique=True)
    fichier=models.FileField(upload_to="fichier")
    def get_fichier_nom(self):
        return self.fichier.name
    def get_url(self):
        return self.fichier.url
    
