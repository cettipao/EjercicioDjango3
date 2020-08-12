from django.db import models

# Create your models here.

STATUS_CHOICES = [
        ('LI', 'Libre'),
        ('PR', 'Prestado'),
        ('RE', 'En Reparacion'),
    ]
class Material(models.Model):
    tipoMaterial = models.CharField(max_length = 30)
    codigo = models.CharField(max_length = 30)
    autor = models.CharField(max_length = 30)
    titulo = models.CharField(max_length = 30)
    anio = models.IntegerField()
    
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='LI',
    )

class Editorial(models.Model):
    nombre = models.CharField(max_length = 30)
class Libro(Material):
    editorial = models.ForeignKey(
        'Editorial',
        on_delete=models.CASCADE,
        null=False
    )

class Revista(Material):
    pass
