from django.db import models

# Create your models here.
class VideoSlide(models.Model):
    video = models.FileField(upload_to='slidevideo')
    caption = models.CharField(max_length=255)
    sub_headding = models.CharField(max_length=255)
    date_updated = models.DateField(auto_now_add=True)