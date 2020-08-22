from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import WorkBlog, HomeBlog
# Create your views here.

def work_blog_list(request):
    MAX_OBJECTS = 20
    work_blog = WorkBlog.objects.all()[:MAX_OBJECTS]
    data = {
        'results': list(work_blog.values('title',\
            'author__username', 'content', 'date_posted'))
    }
    return JsonResponse(data)

def work_blog_detail(request, pk):
    work_blog = get_object_or_404(WorkBlog, pk=pk)
    data = {
        'results':{
            'title': work_blog.title,
            'author': work_blog.author.username,
            'content': work_blog.content,
            'date_posted': work_blog.date_posted
        }
    }
    return JsonResponse(data)


def home_blog_list(request):
    MAX_OBJECTS = 20
    home_blog = HomeBlog.objects.all()[:MAX_OBJECTS]
    data = {
        'results': list(home_blog.values('title',\
            'author', 'content', 'date_posted'))
    }
    return JsonResponse(data)

def home_blog_detail(request, pk):
    home_blog = get_object_or_404(HomeBlog, pk=pk)
    data = {
        'results':{
            'title': home_blog.title,
            'author': home_blog.author.username,
            'content': home_blog.content,
            'date_posted': home_blog.date_posted
        }
    }
    return JsonResponse(data)