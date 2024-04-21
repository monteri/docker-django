from celery import shared_task
import requests
import uuid
from django.conf import settings

PICTURES_URL = "http://placeimg.com/640/480/people"

@shared_task
def download_image():
    response = requests.get(PICTURES_URL)
    file_ext = response.headers.get('Content-Type').split('/')[1]
    file_name = settings.BASE_DIR / 'images' / (str(uuid.uuid4()) + '.' + file_ext)
    with open(file_name, 'wb') as f:
        # for chunk in response.iter_content(chunk_size=128):
        f.write(response.content)
    return True
