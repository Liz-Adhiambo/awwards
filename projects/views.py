import random
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from projects.forms import RatingForm
from django.template import loader
from django.db.models import Avg
from users.models import Profile
from.models import  Project, Rating
from itertools import chain

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer
from rest_framework import status






# Create your views here.




@login_required(login_url='signin')
def uploads(request):
    return render(request,'uploads.html')

@login_required(login_url='signin')
def upload(request):
    

    if request.method == 'POST':
        user = request.user.username
        project_tittle=request.POST['project_tittle']
        project_image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        project_url = request.POST['project_url']
        project_repo = request.POST['project_repo']
        


        new_post = Project.objects.create(user=user,project_tittle=project_tittle, project_image=project_image, caption=caption,project_url=project_url,project_repo=project_repo)
        new_post.save()

        return redirect('projects')
    else:
        return redirect('projects')

@login_required(login_url='signin')
def view_post(request,pk):
    # post_id = request.GET.get('id')
    project = Project.objects.get(id=pk)

    user_object = request.user
    user_profile = Profile.objects.get(user=user_object)




    ratings = Rating.objects.filter(project=project)
    reviews_avg = ratings.aggregate(Avg('design'))
    ureviews_avg=ratings.aggregate(Avg('usability'))
    creviews_avg=ratings.aggregate(Avg('content'))

    reviews_count = ratings.count()
    
    # try:
    #     # post = Post.objects.get(id=post_id)
    # comments = Comment.objects.filter(post__icontains=id)
    #     # print(comments)
        
    # except ObjectDoesNotExist:  
    #     comments = None
    #     post=None
    
    context = {
        'project':project,
        'reviews': ratings,
		'reviews_avg': reviews_avg,
		
        'ureviews_avg':ureviews_avg,
        'creviews_avg':creviews_avg,
        'reviews_count': reviews_count,
        'user_profile': user_profile
        }   
    return render(request,'view_project.html',context)

  
@login_required(login_url='signin')
def projects(request):
    user_object = request.user
    user_profile = Profile.objects.get(user=user_object)
    
    images = Project.objects.all()

    
    # feed = []

    
    
    # feed_lists = Project.objects.all()
    # feed.append(feed_lists)

    # feed_list = list(chain(*feed))

   
    
    

    return render(request,'projects.html' ,{"images":images,'user_profile': user_profile,})

@login_required(login_url='signin')
def Rate(request, pk):
	project = Project.objects.get(id=pk)
	user = request.user

    
    


	if request.method == 'POST':
		form = RatingForm(request.POST)
		if form.is_valid():
			rate = form.save(commit=False)
			rate.user = user
			rate.project = project
			rate.save()
			return HttpResponseRedirect(reverse('viewpost', args=[pk]))
	else:
		form = RatingForm()

	template = loader.get_template('rate.html')

	context = {
		'form': form, 
		'project': project,
	}

	return HttpResponse(template.render(context, request))


# @login_required(login_url='signin')
# def search(request):
#     user_object = User.objects.get(username=request.user.username)
#     user_profile = Profile.objects.get(user=user_object)

#     if request.method == 'POST':
#         username = request.POST['username']
#         username_object = User.objects.filter(username__icontains=username)

#         username_profile = []
#         username_profile_list = []

#         for users in username_object:
#             username_profile.append(users.id)

#         for ids in username_profile:
#             profile_lists = Profile.objects.filter(id_user=ids)
#             username_profile_list.append(profile_lists)
        
#         username_profile_list = list(chain(*username_profile_list))
#     return render(request, 'search.html', {'user_profile': user_profile, 'username_profile_list': username_profile_list})


class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
        
@login_required(login_url='signin')
def search(request):
    project_objects = Project.objects.all()
    user_object = request.user
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        project = request.POST['project']
        project_objects = Project.objects.all()

        
        
        
        
    return render(request, 'search.html', {'project_object': project_objects,'user_profile': user_profile})