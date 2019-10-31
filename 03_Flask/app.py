from flask import Flask, render_template, request
import random, requests
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World'
    return render_template('index.html')
    # root 디렉토리에 있는 templates라는 폴더를 탐색하여 파일을 찾음

@app.route('/ace')
def ace():
    return '불기둥!'

@app.route('/html')
def html():
    return '<h1> 태그 사용할 수 있어요! <h1>'

@app.route('/html_multiline')

# 동적 라우팅
@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('index.html', html_name=name)

#세제곱을 되돌려주는 cube 페이지 작성!
#사용자에게 숫자값을 받아서, 세제곱한 결과를 보여주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    return render_template('cube.html',number=number, result=result)

@app.route('/movies')
def movies():
    movie_list = ['82년생김지영', '조커', '엔드게임', '궁예']
    return render_template('movies.html', movies=movie_list)

# ping : 사용자로부터 입력을 받을 form 페이지를 넘겨준다
@app.route('/ping')
def ping():
    return render_template('ping.html')

# pong : 사용자로부터 form 데이터를 전달받아서 가공한다
@app.route('/pong')
def pong():
    user_name = request.args.get('user_name')
    return render_template('pong.html', user_name=user_name)

# fake naver, google
@app.route('/naver')
def naver():
    return render_template('naver.html')

# 사용자로부터 이름을 입력받을 Form 페이지!
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

# 전달받은 이름을 기준으로 넘겨줄 각종 정보를 가공해서 돌려주는 (응답)로직!
@app.route('/godmademe')
def godmademe():
    # 1. 사용자가 입력한 데이터를 가져온다.
    name = request.args.get('user_name')
    # 2. 사용자에게 보여줄 여러가지 재밌는 특성들 리스트를 만든다.
    first_list = ['잘생김','못생김','개성','키','몸무게','노안','동안','오징어']
    second_list = ['게으름','성실함','근면함','낭비벽','신중함','덜렁거림','귀찮음']
    third_list = ['식욕','똘끼','허세','우울함','가벼움']
    # 3. 리스트에서 랜덤으로 하나씩을 선택한다.
    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)
    # 4. 가공한 정보를 템플릿에 담아서 사용자에게 보여준다.
    return render_template('godmademe.html', name=name, first=first, second=second, third=third)

# 1. 사용자로부터 임의의 텍스트를 입력받아서, 아스키 아트로 변환해서 돌려준다.
# 2. 이 때, 아스키 아트 폰트는 랜덤으로 하나를 지정해서 변환한다
@app.route('/catch')
def catch():
    return render_template('catch.html')

@app.route('/result')
def result():
    # 1. 사용자가 입력한 Form 데이터를 가져온다.
    word = request.args.get("word")
    # 2. ARTII API로 요청을 보내서, 응답 결과를 변수에 담는다. (폰트 정보들)
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3. 가져온 폰트들을 리스트 형태로 바꾼다. -> 줄바꿈(\n)을 기준으로 변수 구분
    fonts = fonts.split('\n')
    # 4. 폰트 하나를 랜덤으로 선택한다.
    font = random.choice(fonts)
    # 5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 담아서 API에게 요청한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    # 6. 최종 결과물을 사용자에게 돌려준다.
    return render_template('result.html', result=result)

# 마지막에 꼭 넣어야 하는 코드
# debug 모드를 활성화해서 서버 새로고침을 생략한다
if __name__ == '__main__':
    app.run(debug=True)