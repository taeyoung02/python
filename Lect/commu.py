import requests
import selenium
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
result=[]
# #문재앙 검색
# for i in range(1,200):
#     url = "https://www.ilbe.com/list/politics?page={}&searchType=title&search=%EB%AC%B8%EC%9E%AC%EC%95%99".format(i)
    
#     r=requests.get(url)
#     bs=BeautifulSoup(r.text,"lxml")#파싱
#     titlelist = bs.findAll("a", {"class":"subject"})
    
#     for title in titlelist[1:]:
#         result.append(title.get_text())
#     print(result[i*20])


# ilbe2 = pd.DataFrame(
#     {
#         'title' : result,
# })

# ilbe2 = ilbe2.drop_duplicates('title', keep='first')
# ilbe2.to_excel('ilbe.xlsx')

# for i in range(1,200):
#     url = "https://www.ilbe.com/list/politics?page={}&searchType=title&search=%EB%AC%B8%EC%9E%AC%EC%95%99".format(i)
    
#     r=requests.get(url)
#     bs=BeautifulSoup(r.text,"lxml")#파싱
#     titlelist = bs.findAll("a", {"class":"subject"})
    
#     for title in titlelist[1:]:
#         result.append(title.get_text())
#     print(result[i*20])


# ilbe = pd.DataFrame(
#     {
#         'title' : result,
# })
# len(libe)
# ilbe2 = ilbe.drop_duplicates('title', keep='first')
# len(libe)
# ilbe2.to_excel('ilbe.xlsx')


# for i in range(0,51):
#     url = "https://www.clien.net/service/search?q=%EB%AC%B8%ED%94%84&sort=accuracy&p={}".format(i)
#     r=requests.get(url)
#     bs=BeautifulSoup(r.text,"lxml")#파싱
#     titlelist = bs.findAll("a", {"class":"subject_fixed"})
    
#     for title in titlelist:
#         title=title.get_text()
#         result.append(title)


# clien = pd.DataFrame(
#     {
#         'title' : result,
#     })

# clien.to_excel('clien.xlsx')

# result2=[]

# for i in range(0,51):
#     url = "https://www.clien.net/service/search?q=%EB%AC%B8%ED%86%B5&sort=accuracy&p={}".format(i)
    
#     r=requests.get(url)
#     bs=BeautifulSoup(r.text,"lxml")#파싱
#     titlelist = bs.findAll("a", {"class":"subject_fixed"})
    
#     for title in titlelist:
#         title=title.get_text()
#         result2.append(title)


# clien = pd.DataFrame(
#     {
#         'title' : result2,
#     })

# clien.to_excel('clien2.xlsx')

# titlelist = pd.read_excel('ilbe.xlsx')
# titlelist = titlelist.drop_duplicates('title', keep='first')

# import requests
# for j in range(0,3):
#     for i in range(1,100):
#         url = 'https://m.cafe.daum.net/moonfan/search/title?query=%EB%8C%80%ED%86%B5%EB%A0%B9&r=https://m.cafe.daum.net/moonfan&sort={}&page={}'.format(j,i)    
        
#         r=requests.get(url)
#         bs=BeautifulSoup(r.text,"lxml")#파싱
#         titlelist = bs.findAll("strong", {"class":"tit_info"})
    
#         for title in titlelist:
#             result.append(title.get_text())
#             print(title.get_text())
# print(len(result))
# moon = pd.DataFrame(
#     {
#         'title' : result,
#     })

# moon = moon.drop_duplicates('title', keep='first')
# moon.to_excel('moon6.xlsx')


# result2=[]

# import requests
# for j in range(0,3):
#     for i in range(1,100):
#         url = 'https://m.cafe.daum.net/moonfan/search/title?query=%EB%AC%B8%EC%9E%AC%EC%9D%B8&r=https://m.cafe.daum.net/moonfan&sort={}&page={}'.format(j,i)    
        
#         r=requests.get(url)
#         bs=BeautifulSoup(r.text,"lxml")#파싱
#         titlelist = bs.findAll("strong", {"class":"tit_info"})
    
#         for title in titlelist:
#             result2.append(title.get_text())
#             print(title.get_text())
# print(len(result2))
# moon = pd.DataFrame(
#     {
#         'title' : result2,
#     })

# moon = moon.drop_duplicates('title', keep='first')
# moon.to_excel('moon5.xlsx')





# result3=[]

# import requests
# for j in range(0,3):
#     for i in range(1,20):
#         url = 'https://m.cafe.daum.net/moonfan/search/title?query=%EB%AC%B8%ED%94%84&r=https://m.cafe.daum.net/moonfan&sort={}&page={}'.format(j,i)    
        
#         r=requests.get(url)
#         bs=BeautifulSoup(r.text,"lxml")#파싱
#         titlelist = bs.findAll("strong", {"class":"tit_info"})
    
#         for title in titlelist:
#             result3.append(title.get_text())
#             print(title.get_text())
# print(len(result3))
# moon = pd.DataFrame(
#     {
#         'title' : result3,
#     })

# moon = moon.drop_duplicates('title', keep='first')
# moon.to_excel('moon4.xlsx')




# result4=[]

# import requests
# for j in range(0,3):
#     for i in range(1,20):
#         url = 'https://m.cafe.daum.net/moonfan/search/title?query=%EB%AC%B8%ED%86%B5&r=https://m.cafe.daum.net/moonfan&sort={}&page={}'.format(j,i)    
        
#         r=requests.get(url)
#         bs=BeautifulSoup(r.text,"lxml")#파싱
#         titlelist = bs.findAll("strong", {"class":"tit_info"})
    
#         for title in titlelist:
#             result4.append(title.get_text())
#             print(title.get_text())
# print(len(result4))
# moon = pd.DataFrame(
#     {
#         'title' : result4,
#     })
# moon = moon.drop_duplicates('title', keep='first')
# print(len(moon))
# moon.to_excel('moon3.xlsx')
    # print(result[i*20])
# titlelist.to_excel('ilbe.xlsx')
# from selenium import webdriver
# import keyboard
# driver = webdriver.Chrome('C://Users//dhrms//Downloads//chromedriver_win32\\chromedriver.exe')#,chrome_options=options)
# driver.get('http://cafe.daum.net/moonfan')
# # driver.get('https://www.instagram.com/{}/'.format(input_target_id))
# #첫번째 게시글 클릭
# #TITLESEARCH > div > input
# driver.implicitly_wait(20)
    
# r=requests.get(driver.current_url)

# _json = r.json()




# m1 = pd.read_excel('moon3.xlsx')
# m2 = pd.read_excel('moon4.xlsx')
# m3 = pd.read_excel('moon5.xlsx')
# m4 = pd.read_excel('moon6.xlsx')
# M=pd.concat([m1,m2,m3,m4])
# M = M.drop_duplicates('title', keep='first')
# M.to_excel('Moon.xlsx')


# I1 = pd.read_excel('ilbe.xlsx')
# I2 = pd.read_excel('ilbe3.xlsx')
# I=pd.concat([I1,I2])
# I = I.drop_duplicates('title', keep='first')
# I.to_excel('Ilbe0.xlsx')

# C1 = pd.read_excel('Clien.xlsx')
# C2 = pd.read_excel('clien2.xlsx')
# C=pd.concat([C1,C2])
# C = C.drop_duplicates('title', keep='first')
# C.to_excel('Clien0.xlsx')

#문재인
# result3=[]
# import requests
# for i in range(1,170):
#     url = 'http://www.todayhumor.co.kr/board/list.php?table=&page={}&kind=search&keyfield=subject&keyword=%EB%AC%B8%EC%9E%AC%EC%9D%B8'.format(i)    
    
#     r=requests.get(url)
#     bs=BeautifulSoup(r.text,"lxml")#파싱
#     titlelist = bs.findAll("tr", {"class":"view list_tr_sisa"})
    
#     for title in titlelist:
#         recommand=title.find("td", {"class":"oknok"}).get_text()
        
#         if '/' not in recommand:
#             title=title.find("td", {"class":"subject"}).get_text()
#             if '"' not in title:
#                 result3.append(title)
#                 print(title)
            

# print(len(result3))
# OU = pd.DataFrame(
#     {
#         'title' : result3,
#     })

# OU = OU.drop_duplicates('title', keep='first')
# OU.to_excel('OU.xlsx')


# #문프
# result8=[]
# import requests
# for i in range(1,34):
#     url = 'http://www.todayhumor.co.kr/board/list.php?table=&page={}&kind=search&keyfield=subject&keyword=%EB%AC%B8%ED%94%84'.format(i)    
    
#     r=requests.get(url)
#     bs=BeautifulSoup(r.text,"lxml")#파싱
#     titlelist = bs.findAll("tr", {"class":"view list_tr_sisa"})
    
#     for title in titlelist:
#         recommand=title.find("td", {"class":"oknok"}).get_text()
#         if '/' not in recommand:
#             title=title.find("td", {"class":"subject"}).get_text()
#             if '"' not in title: #뉴스기사 인용 제외
#                 result8.append(title)
#                 print(title)
            

# print(len(result8))
# OU2 = pd.DataFrame(
#     {
#         'title' : result8,
#     })

# OU2 = OU2.drop_duplicates('title', keep='first')
# OU2.to_excel('OU2.xlsx')


OU2 = pd.read_excel('OU2.xlsx')
OU = pd.read_excel('OU.xlsx')
OU2['title'] = OU2['title'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
OU['title'] = OU['title'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")


OU=pd.concat([OU2,OU])
OU =  OU.drop_duplicates('title', keep='first')
OU.to_excel('OU3.xlsx')