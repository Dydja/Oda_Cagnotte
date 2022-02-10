from tabnanny import verbose
from django.db import models

# Create your models here.

#model academicien

class Academician(models.Model):
    last_name = models.CharField(max_length=30 , verbose_name="nom")
    first_name = models.CharField(max_length=40, verbose_name="prenom")
    register_number = models.CharField(max_length=30,verbose_name="matricule")
    picture = models.FileField(upload_to="pictures" , verbose_name="photos")
#qu'il renomme le nom de la table par academicine
    class Meta:
        verbose_name = "Academicien"

    #recupere l'object sous forme d'objects
    def __str__(self) -> str:
        return self.last_name