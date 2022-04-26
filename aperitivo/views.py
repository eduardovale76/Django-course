from django.shortcuts import render

    
videos = [
   # {'slug':'motivacao','titulo':'Video Aperitivo: Motivação', 'youtube_id':'23tusPiiNZk'},
    #{'slug':'instalacao-windows', 'titulo':'Instalação Windows', 'youtube_id':'QZ1ASyiq-NQ'},
]

videos_dct = {dct['slug']: dct for dct in videos}  

def indice(request):
    return render(request, 'aperitivo/indice.html', context={'videos': videos})

def video(request,slug):
    video = videos_dct[slug]
    
    return render(request, 'aperitivo/video.html', context={'video':video})
