import os
import cloudinary.uploader
from django.conf import settings
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

MEDIA_DIR = os.path.join(settings.BASE_DIR, 'media')

for root, dirs, files in os.walk(MEDIA_DIR):
    for file in files:
        local_path = os.path.join(root, file)
        rel_path = os.path.relpath(local_path, MEDIA_DIR)
        cloudinary_path = rel_path.replace("\\", "/")  # Windows compatibility

        print(f"Uploading {cloudinary_path}...")

        cloudinary.uploader.upload(
            local_path,
            public_id=cloudinary_path,
            resource_type="image",
            overwrite=True,
        )
