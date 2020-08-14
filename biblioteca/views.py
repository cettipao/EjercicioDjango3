from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Libro,Revista

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Libro.objects.all()
        context['revistas'] = Revista.objects.all()
        return context