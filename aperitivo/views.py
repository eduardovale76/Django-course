from django.shortcuts import render

class Video:
    def __init__(self, slug, titulo, youtube_id):
        self.slug = slug
        self.titulo = titulo
        self.youtube_id = youtube_id
        
videos = [
   Video('motivacao','Video Aperitivo: Motivação', '23tusPiiNZk'),
   Video('instalacao-windows', 'Instalação Windows', 'QZ1ASyiq-NQ'),
]

videos_dct = {v.slug: v for v in videos}  

def indice(request):
    return render(request, 'aperitivo/indice.html', context={'videos': videos})

def video(request,slug):
    video = videos_dct[slug]
    
    return render(request, 'aperitivo/video.html', context={'video':video})
