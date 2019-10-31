# 1. 딕셔너리 만들기
lunch = {
    '중국집' : '032'
}
lunch = dict(중국집='032')

# 2. 딕셔너리 내용 추가하기
lunch['분식집'] = '031'

# 3. 딕셔너리 내용 가져오기 (2가지)
artists = {
    '아티스트': {
        '주니엘': '일라일라',
        '트와이스': '치어업'
    }
}
# 주니엘의 대표곡은?
print(artists["아티스트"]["주니엘"])
print(artists.get("아티스트").get("주니엘"))

# 1. 딕셔너리 반복문 활용하기
# 1.4.1 기본 활용
for key in lunch:
    print(key)          # key 값 출력됨
    print(lunch[key])   # key로 value 추출

# 1.4.2 .items : key, value 모두 가져오기
for key, value in lunch.items():
    print(key, value)

# 1.4.3 .values : value만 가져오기
for value in lunch.values():
    print(value)

# 1.4.4 .keys : key만 가져오기
for key in lunch.keys():
    print(key)

# bit.do/yeoksam_python33