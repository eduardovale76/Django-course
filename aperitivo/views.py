from django.shortcuts import render



def video(request,slug):
    
    videos = {
    'motivacao': {'titulo':'Video Aperitivo: Motivação', 'youtube_id':'23tusPiiNZk'},
    'instalacao-windows': {'titulo':'Instalação Windows', 'youtube_id':'QZ1ASyiq-NQ'},
    }
    
    video = videos[slug]
    
    return render(request, 'aperitivo/video.html', context={'video':video})
