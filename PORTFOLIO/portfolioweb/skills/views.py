from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SkillsView(TemplateView):
    template_name = 'skills.html'