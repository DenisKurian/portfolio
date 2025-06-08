from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Project
from django.conf import settings

class ProjectListView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'

class HomeView(TemplateView):
    template_name = "core/home.html"
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] =settings.MEDIA_URL
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"

class SkillsView(TemplateView):
    template_name = "core/skills.html"

class ProjectsView(TemplateView):
    template_name = "core/projects.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"

