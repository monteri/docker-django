from django.shortcuts import render

from . import tasks

def home(request):
    if request.method == 'POST':
        tasks.download_image.delay()
    return render(request, 'index.html')