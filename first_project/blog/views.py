# Create your views here.

from django.shortcuts import render
from .models import Article



def home(request):
    # return HttpResponse('<h1>Hello on my blog!</h1>')
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': Article.objects.all()})

def about(request):
    """ nowy endpoint about znajdujacy się w first_project/urls.py blog/urls.py """
    # return HttpResponse('<h1>About Us </h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


