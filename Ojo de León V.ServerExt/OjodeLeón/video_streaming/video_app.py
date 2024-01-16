# video_app/models.py

from django.db import models

class VideoConfig(models.Model):
    url = models.CharField(max_length=255)
