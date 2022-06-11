from datetime import datetime
import uuid
from django.db import models
from django.contrib.auth import get_user_model



class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='project_images')
    caption = models.TextField()
    project_url=models.URLField(null=True,blank=True)
    project_repo=models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user