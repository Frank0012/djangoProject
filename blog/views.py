from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from . models import Post


#def index(request):
#    title = "Frank Crossley"
#    return render(request, 'index/index.html', {'title':title})

def about(request):
    title = "About"
    return render(request, 'about/about.html', {'title':title})

def CV(request):
    title = "CV"
    return render(request, 'CV/CV.html', {'title':title})

def projects(request):
    title = "Projects"
    return render(request, 'projects/projects.html', {'title':title})

def post_list(request):
    title = "Blog"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog.html', {'posts':posts, 'title':title})
