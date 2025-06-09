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
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_projects = Project.objects.all()

        # Group projects into chunks of 3
        def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i + n]

        context['project_chunks'] = list(chunks(all_projects, 3))
        context['MEDIA_URL'] =settings.MEDIA_URL
        context['projects'] = Project.objects.all()
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"

class SkillsView(TemplateView):
    template_name = "core/skills.html"

class ProjectsView(TemplateView):
    template_name = "core/projects.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"

