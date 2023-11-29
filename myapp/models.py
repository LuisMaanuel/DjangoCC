from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)
    nodos = models.CharField(max_length=100)
    num_cores = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    almacenamiento = models.CharField(max_length=100)
    teraFlops = models.CharField(max_length=100)
    SO = models.CharField(max_length=100)
    