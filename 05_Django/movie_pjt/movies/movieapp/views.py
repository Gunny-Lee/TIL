from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):
    movie = Movie.objects.all()[::-1]
    context = {'movieapp': movie}
    return render(request, 'movieapp/index.html', context)

def new(request):
    return render(request, 'movieapp/new.html')

def create(request):
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
    movie.save()
    return redirect('/movieapp/')

# 게시글 상세정보를 가져오는 함수
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie': movie}
    return render(request, 'movieapp/detail.html', context)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('/movieapp/')
    
# 사용자에게 수정 폼 던져줌
def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie': movie}
    return render(request, 'movieapp/edit.html', context)

# 데이터 받아서 DB에 반영
def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.title = request.POST.get('title')
    movie.title_en = request.POST.get('title_en')
    movie.audience = request.POST.get('audience')
    movie.open_date = request.POST.get('open_date')
    movie.genre = request.POST.get('genre')
    movie.watch_grade = request.POST.get('watch_grade')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    # return redirect(f'/articles/{article.pk}/')       # 1. 하드코딩
    return redirect('movieapp:detail', movie.pk) # 2. URL Namespace

    # .html 파일 내에서 '{% url %} 템플릿 태그' 사용햇을 때(헷갈림 주의!!!!)
    # <a href="{% url articles:detail article.pk %}">