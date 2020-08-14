from django.contrib import admin
from .models import *
# Register your models here.

class PrestamoInLine(admin.TabularInline): #Para ver los prestamos de la persona
    model = Prestamo

class AlumnoAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    search_fields = ['nombre', 'apellido', 'correo', 'telefono','matricula']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido',)
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono',)
        }),
        ('Alumno', {
            'fields': ('matricula',)
        }),
    )

class ProfesorAdmin(admin.ModelAdmin):
    inlines = [PrestamoInLine, ]
    search_fields = ['nombre', 'apellido', 'correo', 'telefono', 'numEmpleado']
    fieldsets = (
        ("Persona", {
            'fields': ('nombre', 'apellido',)
        }),
        ('Contacto', {
            'fields': ('correo', 'telefono',)
        }),
        ('Empleado', {
            'fields': ('numEmpleado',)
        }),
    )

admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Prestamo)
