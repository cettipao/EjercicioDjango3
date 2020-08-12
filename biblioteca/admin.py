from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Prestamo)