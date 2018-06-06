from django.db import models

# Create your models here.
class Pdf(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    FechaCreacion = models.DateField('Fecha de creación', auto_now_add=True)
    Upload = models.FileField('Archivo')

    def __str__(self):
        return self.Nombre