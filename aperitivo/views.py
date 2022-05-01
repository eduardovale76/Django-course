from unittest.util import _MAX_LENGTH
from django.shortcuts import render, get_object_or_404
from .models import Video

        
videos = [
   Video(slug='motivacao',titulo='Video Aperitivo: Motivação', youtube_id='23tusPiiNZk'),
   Video(slug='instalacao-windows', titulo='Instalação Windows', youtube_id='QZ1ASyiq-NQ'),
]

videos_dct = {v.slug: v for v in videos}  

def indice(request):
    return render(request, 'aperitivo/indice.html', context={'videos': videos})

def video(request,slug):
    video = get_object_or_404(Video, slug=slug)
    
    return render(request, 'aperitivo/video.html', context={'video':video})
