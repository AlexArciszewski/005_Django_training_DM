# Create your views here.

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article



def home(request):
    # return HttpResponse('<h1>Hello on my blog!</h1>')
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': Article.objects.all()})

def about(request):
    """ nowy endpoint about znajdujacy się w first_project/urls.py blog/urls.py """
    # return HttpResponse('<h1>About Us </h1>')
    return render(request, 'blog/about.html', {'title': 'About'})


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
