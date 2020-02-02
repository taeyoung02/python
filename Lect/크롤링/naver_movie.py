import requests
from bs4 import BeautifulSoup
import pandas as pd
#select는 만족하는 여러 인스턴스를 찾고, find는 첫 번째 인스턴스를 반환합니다.
def get_movie_point(start, end):
    result = []
    for i in range(start, end+1):
        url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'.format(i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")

        trs = bs.select("table.list_netizen > tbody > tr")
        for tr in trs:#다수의 평점
            # td = tr.select("td")
            # title= td[1].select("a")[0].text
            # score=tr.find("div",{"class":"list_netizen_score"}).find("em").text
            # print(title, score)

            tr_data = tr.find("td",{"class":"title"})
            title=tr_data.find("a").text
            score=tr_data.find("em").text
            # print("{} : {}점".format(title, score))
            tr_data.find("a").extract()
            tr_data.find("div").extract()
            tr_data.find("a").extract()
            content=tr_data.text.strip()
            # if not content=="":
            #     print(content)
            # print()
            result.append([title, score, content])

            # content=tr.find("td",{"class","title"}).text
            # content=content.split('\n')
            # content="\n".join(content[0:6])
            # print(content)
            # print()
    return result
column = ["제목", "점수", "감상평"]
result = get_movie_point(1,10)
dataframe= pd.DataFrame(result, columns=column)#차트형식을로 바꿔줌
print(dataframe)

dataframe.to_excel("movie.xlsx", sheet_name="네이버영화", header=True,startrow=0)
#엑셀에 저장