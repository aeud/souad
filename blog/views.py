from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from blog.models import Article
from blog.forms import ArticleForm

def home(request): #https://docs.djangoproject.com/en/1.9/ref/request-response/
    
    articles = Article.objects.all().order_by('created_at')[:10] #10 last articles

    return render(request, 'home.html', dict(articles=articles,)) # response

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    form = ArticleForm(dict(title=title,
                            content=content,))
    if form.is_valid():
        article = Article(title=title, content=content,)
        article.save()
    #else:
        #return 
    return redirect(show, article_id=article.id)

def show(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'show.html', dict(article=article,))

def edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'edit.html', dict(article=article,))

def update(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    form = ArticleForm(dict(title=title,
                            content=content,))
    if form.is_valid():
        article.title = title
        article.content = content
        article.save()
    #else:
        #return 
    return redirect(show, article_id=article.id)