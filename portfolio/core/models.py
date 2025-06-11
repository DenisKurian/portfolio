
from django.db import models
import os
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_demo_url = models.URLField(blank=True, null=True)
    source_code_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Certificates(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='certificates/')
    thumbnail = models.ImageField(upload_to='certificate_thumbnails/', blank=True, null=True)

    def get_or_generate_thumbnail(self):
        from .utils import generate_thumbnail
        import os

        if self.thumbnail:
            return self.thumbnail.url  # ✅ Already generated

        if self.file and self.file.name.lower().endswith('.pdf'):
            thumb = generate_thumbnail(self.file.path)
            if thumb:
                name = os.path.splitext(os.path.basename(self.file.name))[0] + "_preview.jpg"
                self.thumbnail.save(name, thumb, save=True)
                return self.thumbnail.url
        return None
    def __str__(self):
        return self.title
    
class Skills(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

