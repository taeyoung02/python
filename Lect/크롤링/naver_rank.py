import requests
from bs4 import BeautifulSoup

# 2020년 1월 18일 부로 네이버 실시간 검색어 데이터가 페이지 임베딩방식에서
# ajax 통신으로 변경되어서 기존 코드 수정
# 아래 주소가 메인페이지 내부에서 호출되는 실시간 검색어 데이터를 넘겨주는 주소
# request.get("주소").json() 을 하면 데이터를 json 형태로 받아올 수 있습니다.

json = requests.get('https://www.naver.com/srchrank?frm=main').json()

# json 데이터에서 "data" 항목의 값을 추출
ranks = json.get("data")

#해당 값은 리스트 형태로 제공되기에 리스트만큼 반복
for r in ranks:
    rank=r.get("rank")
    keyword=r.get("keyword")
    print(rank, keyword)

