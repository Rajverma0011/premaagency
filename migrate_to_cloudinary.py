import os
from dotenv import load_dotenv
import django

# LOAD ENV VARIABLES
load_dotenv()

# DEBUG CHECK (temporary)
print("API KEY:", os.getenv("API_KEY"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import cloudinary

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)
from tiles.models import Tile, Sanitary
import cloudinary.uploader


def upload_image(instance, field_name):
    field = getattr(instance, field_name)

    if not field:
        return

    file_path = field.path

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        print(f"⬆ Uploading: {file_path}")

        response = cloudinary.uploader.upload(file_path)

        field.name = response['public_id'] + "." + response['format']
        instance.save()

        print(f"✅ Uploaded: {response['secure_url']}")

    except Exception as e:
        print(f"❌ Error: {e}")


def migrate_tiles():
    for tile in Tile.objects.all():
        upload_image(tile, 'image')


def migrate_sanitary():
    for item in Sanitary.objects.all():
        upload_image(item, 'image')


if __name__ == "__main__":
    print("🚀 Starting migration...")
    migrate_tiles()
    migrate_sanitary()
    print("🎉 Done!")