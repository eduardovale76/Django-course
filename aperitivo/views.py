from django.shortcuts import render



def video(request,slug):
    video = {
    'titulo':'Video Aperitivo: Motivação',
    'youtube_id':'23tusPiiNZk',
}
    return render(request, 'aperitivo/video.html', context={'video':video})
