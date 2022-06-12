import random
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from itertools import chain

from users.models import Profile
from.models import  Project
# Create your views here.


def uploads(request):
    return render(request,'uploads.html')

def upload(request):

    if request.method == 'POST':
        user = request.user.username
        project_image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        project_url = request.POST['project_url']
        project_repo = request.POST['project_repo']


        new_post = Project.objects.create(user=user, project_image=project_image, caption=caption,project_url=project_url,project_repo=project_repo)
        new_post.save()

        return redirect('/')
    else:
        return redirect('/')

def view_post(request,pk):
    # post_id = request.GET.get('id')
    project = Project.objects.get(id=pk)
    
    
    # try:
    #     # post = Post.objects.get(id=post_id)
    # comments = Comment.objects.filter(post__icontains=id)
    #     # print(comments)
        
    # except ObjectDoesNotExist:  
    #     comments = None
    #     post=None
    
    context = {
        'project':project,
        
        }   
    return render(request,'view_project.html',context)

def projects(request):
    
    
    images = Project.objects.all()

    
    # feed = []

    
    
    # feed_lists = Project.objects.all()
    # feed.append(feed_lists)

    # feed_list = list(chain(*feed))

   
    
    

    return render(request,'projects.html' ,{"images":images,})
