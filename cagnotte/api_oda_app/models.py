from email import charset
from tabnanny import verbose
from django.db import models

# Create your models here.

#model academicien

class Base(models.Model):
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Academician(Base):
    last_name = models.CharField(max_length=30 , verbose_name="nom")
    first_name = models.CharField(max_length=40, verbose_name="prenom")
    register_number = models.CharField(max_length=30,verbose_name="matricule")
    picture = models.FileField(upload_to="pictures" , verbose_name="photos")

    class Meta:
        verbose_name = "Academicien"
        verbose_name_plural = "Academiciens"
    
    def __str__(self):
        return self.last_name

class Motif(Base):
    nom_motif = models.ForeignKey(Academician, related_name="motif_academician",verbose_name=("Academicien"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Motif"
        verbose_name_plural = "Motifs"

    def __str__(self):
        return self.nom_motif


class payment(Base):
    register_number = models.CharField(max_length=50)
    motif = models.CharField(max_length=255)
    montant = models.CharField(max_length=255)


