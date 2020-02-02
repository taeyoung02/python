import requests # 웹상의 웹페이지를 다운로드하는 역할,소스보기 했을때 나오는 코드를 다운로드 하는 라이브러리
from bs4 import BeautifulSoup
import json#ajax를 위한 데이터 형식. dictionary format 
#서버로부터 웹페이지가 반환되면 화면 전체를 갱신해야 하는데 페이지 일부만을 갱신하고도 동일한 효과를 볼 수 있도록 하는 것이 Ajax
import geohash2

#pip install bs4
#pip install requests
#pip install geohash2
#pip install pprint

while True:
    keyword = input("찾고자하는 지역을 입력하세요(ex.철산동/철산역/광명시) : ")

    # 최초 검색어에 해당하는 검색어값의 자동완성 ajax 주소
    url = "https://apis.zigbang.com/search?q={}".format(keyword)

    req = requests.get(url)

    # 실제 api 주소에서 json 형태로 리턴되기 때문에 json 형태로 값을 받는다.
    # json 형태로 받은 값은 사용하기편리
    _json = req.json()

    # api 상태코드가 200인 경우가 오류없이 동작되었다는 의미
    if _json.get("code") == "200":
        #리스트items의 0번째 요소
        Data = _json.get("items")[0]
        _description = Data.get("description")
        _id = Data.get("id")
        _lat = Data.get("lat")
        _lng = Data.get("lng")
        _zoom = Data.get("zoom")

        geohash = geohash2.encode(_lat, _lng, precision=5)

        # 위에서 구한 geohash 값을 아래의 api 로 호출하고 쿼리(전세 월세 등)를 넘겨주는 주소
        url = "https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={}&rent_gteq=0&sales_type_in=전세%7C월세&service_type_eq=원룸".format(geohash)

        #json 형태로
        _req_items = requests.get(url).json()

        # json 데이터에서 items 값만 저장
        # items 값은 실제 매물 데이터의 인덱스 값
        _items = _req_items.get("items")

    if not _items:
        print("좀 더 번화가를 찾아보시죠")
    else: break

# 위에서 취한 json 형태의 items 목록을 저장
item_ids = []
for item in _items:
    item_ids.append(item.get("item_id"))

# 위에서 저장한 list 의 100개만
# items_ids 라는 키의 값으로 설정
# 이 값을 직방 api 에 요청
items = {"item_ids": item_ids[:200]}
# 위에서 만든 items_ids: [매물인덱스] 를 아래 주소로 쿼리 한 후 json 형태로 받는다
_results = requests.post('https://apis.zigbang.com/v2/items/list', data=items).json()

# 최종 완성된 매물 결과는 items 안에 있다
Datas = _results.get("items")

house=input("아파트/빌라/원룸/오피스텔> ")
pay=input("전세/월세> ")
cost=input("수용가능한 월세(만원)> ")

for d in Datas:# pprint.pprint(d)
    _address = "{} {}".format(d.get("address1"), d.get("address2"))
    if d.get("address3") is not None:
        _address += " {}".format(d.get("address3"))

    building_floor = d.get("building_floor")
    floor = d.get("floor")
    thumbnail = d.get("images_thumbnail")
    item_id = d.get("item_id")
    reg_date = d.get("reg_date")
    sales_type = d.get("sales_type")
    service_type = d.get("service_type")
    size_m2 = d.get("size_m2")
    title = d.get("title")
    deposit = d.get("deposit")
    rent = d.get("rent")
    
    #아파트, 빌라, 원룸, 오피스텔
    if service_type==house and sales_type==pay and rent<int(cost):#조건설정
        print("*" * 100)
        print("{} ".format(title))
        print("보증금/월세: {}/{}".format(deposit, rent))
        print("건물층/매물층: {}/{}".format(building_floor, floor))
        print("등록일자: {}".format(reg_date))
        print("서비스형태/매물형태: {}/{}".format(service_type, sales_type))
        print("사이즈: {}m^2".format(size_m2))
        if service_type=="원룸":
            _type="oneroom"
        elif service_type=="아파트":
            _type="apt"
        elif service_type=="빌라":
            _type="villa"
        else:
            _type="officetel"
        print("링크 : 'https://www.zigbang.com/home/{}/items/{}'".format(_type, item_id))
