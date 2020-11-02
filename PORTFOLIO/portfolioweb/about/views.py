from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Page

# Create your views here.
class AboutView(TemplateView):
    template_name = 'experiencia.html'


