from django.shortcuts import render
import random, requests
import numpy as np
from datetime import datetime

# Create your views here.
# new 함수 -> 중간 관리자
# 사용자가 접속해서 볼 페이지를 작성한다. 즉, 하나하나의 페이지를 'view'라고 부른다.
# 'view' 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다.
def index(request):  # 첫 번째 인자 반드시 request:
  return render(request, 'index.html')

# 실습1 : 템플릿 변수를 2개이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해 보자
def introduce(request):
  context = {
    'name': '감자',
    'age': '20',
    'hobby': '낚시',
    'good': '노래'
  }
  # render 메서드의 세번째 인자로 변수를 딕셔너리 형태로 넘길 수 있다
  return render(request, 'introduce.html', context)

def dinner(request):
  menu = ['초밥', '삼겹살', '치즈돈까스', '살치살스테이크']
  pick = random.choice(menu)
  context = {
    'pick': pick
  }
  return render(request, 'dinner.html', context)

# Lorem Picsum 사용해서 랜덤 이미지 보여주는 페이지 만들기!
# 추가실습 - 동적 라우팅으로 이미지 너비, 높이를 받아서 이미지 출력하는 페이지!
def image(request, wid, hgt):
  context = {
    'wid': wid,
    'hgt': hgt
  }
  return render(request, 'image.html', context)

# 동적 라우팅
def hello(request, name):
  menu = ['초밥', '삼겹살', '치즈돈까스', '살치살스테이크']
  pick = random.choice(menu)
  context = {
    'name': name,
    'pick': pick
  }
  return render(request, 'hello.html', context)

# 실습 2 : 숫자 2개를 동적 라우팅으로 전달 받아서, 두 개의 숫자를 곱해주는 페이지를 만들자!
def times(request, number, numb):
  result = number * numb
  context = {
    'number': number,
    'numb': numb,
    'result': result
  }
  return render(request, 'times.html', context)

# 실습 3 : 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자!
def area(request, rad):
  result = (rad ** 2) * np.pi
  context = {
    'rad': rad,
    'result': ("%0.4f" %result)
  }
  return render(request, 'area.html', context) 

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

# 실습1. IS IS YOUR BIRTH?
# 오늘 날짜와 본인 실제 생일 비교해서, 맞으면 예! 아니면 아니오!
def isbirth(request):
  nowdate = datetime.now()
  if nowdate.month == 12 and nowdate.day == 25:
    result = True
  else:
    result = False
  context = {'result': result}
  return render(request, 'isbirth.html', context)

# 실습2. 회문 판별 (팰린드롬 / 문자열 슬라이싱 파트 활용)
# ex) 오디오는 거꾸로 해도 오디오 -> 회문!
def ispal(request, word):
  # 검색 키워드 : 파이썬 문자열 슬라이스
  if word == word[::-1]:
    result = True
  else:
    result = False
  context = {
    'word': word,
    'result': result
  }
  return render(request, 'ispal.html', context)

# 실습3. 로또 번호 추첨 (리스트 + a 활용)
# 임의로 출력한 로또 번호와 가장 최근에 추첨한 로또 번호 비교해서 당첨여부 확인
def lotto(request):
  lottos = sorted(list(random.sample(range(1,46), 6)))
  lottodap = [18, 34, 39, 43, 44, 45] # 882 회차
  
  context = {
    'lottos': lottos,
    'lottodap': lottodap
  }
  return render(request, 'lotto.html', context)

