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

class Persona(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    correo = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 30)
    numLibros = models.IntegerField()
    adeudo = models.FloatField()

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    numEmpleado = models.IntegerField()

class Prestamo(models.Model):
    codigo = models.CharField(max_length = 30)
    fechaSalida = models.DateField(auto_now=False)
    fechaRegreso = models.DateField(auto_now=False)
    Persona = models.ForeignKey(
        'Persona',
        on_delete=models.CASCADE,
        null=False
    )
    Material = models.ForeignKey(
        'Material',
        on_delete=models.CASCADE,
        null=False
    )