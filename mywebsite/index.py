from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


    
def index(request):
    title = "Frank Crossley"
    return render(request, 'index/index.html', {'title':title})
