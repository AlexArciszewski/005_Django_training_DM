# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

POSTS = [
    {
      'author': 'Devs-Mentoring.pl',
      'title': 'To be or not to be',
      'content': "This is my first post",
      'date': '28 February 2024'
    },
    {
        'author': 'Devs-Mentoring.pl',
        'title': 'What if...',
        'content': "This is my second post",
        'date': '28 February 2024'


    }
]

def home(request):
    # return HttpResponse('<h1>Hello on my blog!</h1>')
    return render(request, 'blog/home.html', {'title': 'Home', 'posts':POSTS})

def about(request):
    """ nowy endpoint about znajdujacy się w first_project/urls.py blog/urls.py """
    # return HttpResponse('<h1>About Us </h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


