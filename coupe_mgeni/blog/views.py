from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.

def home(request):
    articles= Article.objects.all()
    return render(request, 'blog.html', {'derniers_articles': articles})


def lire(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'article.html', {'article': article})
