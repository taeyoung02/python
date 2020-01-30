import requests # 웹상의 웹페이지를 다운로드하는 역할,소스보기 했을때 나오는 코드를 다운로드 하는 라이브러리
from bs4 import BeautifulSoup
import json#ajax를 위한 데이터 형식. dictionary format 
#서버로부터 웹페이지가 반환되면 화면 전체를 갱신해야 하는데 페이지 일부만을 갱신하고도 동일한 효과를 볼 수 있도록 하는 것이 Ajax
import geohash2
import pprint

#pip install bs4
#pip install requests
#pip install geohash2
#pip install pprint


keyword = "가산디지털단지"

# 최초 검색어에 해당하는 검색어값의 자동완성 ajax 주소
url = "https://apis.zigbang.com/search?q={}".format(keyword)

req = requests.get(url)

# 실제 api 주소에서 json 형태로 리턴되기 때문에 json 형태로 값을 받는다.
# json 형태로 받은 값은 사용하기편리
_json = req.json()

# api 상태코드가 200인 경우가 오류없이 동작되었다는 의미
if _json.get("code") == "200":
    #리스트items의 0번째 요소
    data = _json.get("items")[0]
    _description = data.get("description")
    _id = data.get("id")
    _lat = data.get("lat")
    _lng = data.get("lng")
    _zoom = data.get("zoom")

    geohash = geohash2.encode(_lat, _lng, precision=5)
    print(geohash)
    # 위에서 구한 geohash 값을 아래의 api 로 호출하고 쿼리(전세 월세 등)를 넘겨주는 주소
    url = "https://apis.zigbang.com/v2/items?deposit_gteq=0&domain=zigbang&geohash={}&rent_gteq=0&sales_type_in=전세%7C월세&service_type_eq=원룸".format(geohash)

    #json 형태로
    _req_items = requests.get(url).json()

    # json 데이터에서 items 값만 저장합니다.
    # items 값은 실제 매물 데이터의 인덱스 값입니다.
    _items = _req_items.get("items")

    # 위에서 취한 json 형태의 items 목록을
    # 파이썬 리스트 형태로 저장합니다.
    item_ids = []
    for item in _items:
        item_ids.append(item.get("item_id"))

    # 위에서 저장한 list 의 100개만
    # items_ids 라는 키의 값으로 설정합니다.
    # 최종적으로 이 값을 직방 api 에 요청합니다.
    items = {"item_ids": item_ids[:100]}

    # 위에서 만든 items_ids: [매물인덱스] 를 아래 주소로 쿼리 한 후 json 형태로 받습니다.
    _results = requests.post('https://apis.zigbang.com/v2/items/list', data=items).json()

    # 최종 완성된 매물 결과는 items 안에 있습니다.
    datas = _results.get("items")

    # 매물 목록을 돌며 화면에 출력합니다.
    for d in datas:
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

        if service_type=="원룸" and sales_type=="월세" and rent<50:# pprint.pprint(d)
            print("*" * 100)
            print("{} [{}]".format(title, item_id))
            print("보증금/월세: {}/{}".format(deposit, rent))
            print("건물층/매물층: {}/{}".format(building_floor, floor))
            print("등록일자: {}".format(reg_date))
            print("서비스형태/매물형태: {}/{}".format(service_type, sales_type))
            print("사이즈: {}".format(size_m2))
