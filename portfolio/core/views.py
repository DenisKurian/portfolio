from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Project, Certificates, Skills
from django.conf import settings

emoji_map = {
    "AWS": "☁️",
    "Android": "🤖",
    "Arch Linux": "🎯",
    "BeautifulSoup": "🍜",
    "Blender": "🧡",
    "Bootstrap": "📦",
    "C": "🔵",
    "C#": "🎼",
    "C++": "➕",
    "CSS": "🎨",
    "Django": "🌿",
    "Docker": "🐳",
    "Excel": "📊",
    "FastAPI": "⚡",
    "Figma": "🎨",
    "Firebase": "🔥",
    "Flutter": "💙",
    "Git": "🔧",
    "GitHub": "🐙",
    "GraphQL": "🕸️",
    "HTML": "📄",
    "Illustrator": "✒️",
    "Java": "☕",
    "JavaScript": "✨",
    "Jira": "📋",
    "Keras": "🔬",
    "Linux": "🐧",
    "Matplotlib": "📈",
    "MongoDB": "🍃",
    "MySQL": "🐬",
    "Nginx": "🧭",
    "Node.js": "🌲",
    "Notion": "📓",
    "NumPy": "📐",
    "OpenCV": "👁️",
    "Pandas": "🐼",
    "Photoshop": "🖌️",
    "PostgreSQL": "🐘",
    "Postman": "📮",
    "PowerPoint": "📽️",
    "PyTorch": "🔥",
    "Python": "🐍",
    "REST API": "🔗",
    "React": "⚛️",
    "Regex": "🔍",
    "SQL": "🗄️",
    "SQLite": "📘",
    "Scikit-learn": "📊",
    "Selenium": "🧪",
    "Shell": "💻",
    "Slack": "💬",
    "Streamlit": "🧵",
    "Tailwind": "🌬️",
    "TensorFlow": "🧠",
    "Trello": "🗂️",
    "TypeScript": "🌀",
    "Ubuntu": "🟠",
    "Unity": "🎮",
    "VS Code": "📝",
    "iOS": "📱"
}

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
        context['certificates'] = Certificates.objects.all()
        context['skills'] = Skills.objects.all()
        context['emoji_map'] = emoji_map
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"

class SkillsView(TemplateView):
    template_name = "core/skills.html"

class ProjectsView(TemplateView):
    template_name = "core/projects.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"

