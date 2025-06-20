import os
import cloudinary
from cloudinary.uploader import upload
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

MEDIA_DIR = os.path.join(os.getcwd(), 'media')

for root, dirs, files in os.walk(MEDIA_DIR):
    for filename in files:
        file_path = os.path.join(root, filename)

        # Get relative path within media (e.g. projects/grass.jpeg)
        relative_path = os.path.relpath(file_path, MEDIA_DIR)
        # Remove extension for public_id to avoid duplicates like `.jpg.jpg`
        public_id = os.path.splitext(relative_path)[0].replace("\\", "/")

        print(f"Uploading {file_path} → {public_id}")

        try:
            result = upload(
                file_path,
                public_id=public_id,
                resource_type="auto",
                overwrite=True  # optional: allows replacing existing uploads
            )
            print(f"Uploaded: {result['secure_url']}")
        except Exception as e:
            print(f"Failed to upload {file_path}: {e}")
