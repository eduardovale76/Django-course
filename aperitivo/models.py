from django.urls import reverse
from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    youtube_id = models.CharField(max_length=32)
    creation = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('aperitivo:video', args=(self.slug,))
