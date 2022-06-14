from datetime import datetime
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from users.models import Profile






class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    project_tittle=models.CharField(max_length=50,blank=True)
    project_image = models.ImageField(upload_to='project_images')
    caption = models.TextField()
    project_url=models.URLField(null=True,blank=True)
    project_repo=models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user

    def delete_project(self):
      self.delete()

class Rating(models.Model):
    '''
    This model will contain the ratings for diffrent categories
    '''
    design = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    usability = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    content = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.user.username