import requests
from bs4 import BeautifulSoup
query="파이썬강좌"
def get_search_naver_blog(query, start_page, end_page=None):
    #11=(2-1)*10+1
    #21=(3-1)*10+1
    start = (start_page-1)*10+1
    url="https://search.naver.com/search.naver?where=post&query={}&start={}".format(query,start)
    r=requests.get(url)
    bs=BeautifulSoup(r.text,"lxml")#파싱
    result=[]
    if end_page is None:
        tot_counts = int(bs.select("span.title_num")[0].text.split("/")[-1].replace("건","").replace(",","").strip())
        # tot_counts=tot_counts.split("/")[-1]
        # tot_counts.replace("건","").replace(",","").strip()
        end_page=int(tot_counts/10)
        if tot_counts%10 > 0:
            end_page+=1

        if end_page>900:
            end_page=900

    lis=bs.select("li.sh_blog_top")
    for li in lis:
        try:
            #print(li)
            thumbnail=li.select("img")[0]["src"]#src=이미지의 주소
            title=li.select("dl > dt > a")[0]
            summary=li.select("dl > dd.sh_blog_passage")[0].text

            title_link=title["href"]
            title_text=title.text
            result.append((thumbnail, title_text, title_link, summary))
        except:
            continue
    if start_page<end_page:
        start_page+=1
        result.extend(get_search_naver_blog(query, start_page=start_page, end_page=end_page))

    return result

results = get_search_naver_blog("파이썬강좌",start_page=1)
for result in results:
    print(result)