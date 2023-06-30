from django.shortcuts import render

# Create your views here.
from .models import Skill, Education, Project

def portfolio(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    education = Skill.objects.all()
    context = {'projects': projects, 'skills':skills, 'education':education}
    return render(request, 'portfolio.html', context)