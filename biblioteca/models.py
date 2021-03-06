from django.db import models

# Create your models here.

STATUS_CHOICES = [
        ('LI', 'Libre'),
        ('PR', 'Prestado'),
        ('RE', 'En Reparacion'),
    ]
class Material(models.Model):
    codigo = models.CharField(max_length = 30)
    autor = models.CharField(max_length = 30)
    titulo = models.CharField(max_length = 30)
    anio = models.IntegerField()
    
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='LI',
    )
    def __str__(self):
        return self.titulo

class Editorial(models.Model):
    nombre = models.CharField(max_length = 30)

    def __str__(self):
        return self.nombre

class Libro(Material):
    fotoPortada = models.ImageField(max_length=100, upload_to='portadas/', blank=True)
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

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    numEmpleado = models.IntegerField()

class Prestamo(models.Model):
    codigo = models.CharField(max_length = 30)
    fechaSalida = models.DateField(auto_now=False)
    fechaRegreso = models.DateField(auto_now=False)
    persona = models.ForeignKey(
        'Persona',
        on_delete=models.CASCADE,
        null=False
    )
    material = models.ForeignKey(
        'Material',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return self.codigo