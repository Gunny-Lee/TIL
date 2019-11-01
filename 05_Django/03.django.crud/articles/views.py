from django.shortcuts import render, redirect
from .models import Article

# Create your views here. 마지막 글이 맨 위로 오게 뒤집는게 [::-1]
def index(request):
    articles = Article.objects.all()[::-1]
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# 사용자에게 게시글 작성 폼을 보여주는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    # return render(request, 'articles/create.html')
    return redirect('/articles/')

# 게시글 상세정보를 가져오는 함수
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')

# 사용자에게 수정 폼 던져줌
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)

# 데이터 받아서 DB에 반영
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    # return redirect(f'/articles/{article.pk}/')       # 1. 하드코딩
    return redirect('articles:detail.html', article.pk) # 2. URL Namespace

    # .html 파일 내에서 '{% url %} 템플릿 태그' 사용햇을 때(헷갈림 주의!!!!)
    # <a href="{% url articles:detail article.pk %}">