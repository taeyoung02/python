from bs4 import BeautifulSoup
import requests
import re
import json
import random

url="https://www.usatoday.com/"
r=requests.get(url)
bs=BeautifulSoup(r.text,"lxml")

headlines=bs.select("body > main > div.gnt_rr > div.gnt_m_th > a")
# headlines=headlines[headlines["aria-label"]=="Top Headlines"]
urls=[]

for headline in headlines[0:-1]:
    href=headline["href"]
    urls.append(url+href[0:-1])

contents=""
for i in range(len(urls)):
    url=urls[i]
    r=requests.get(url)
    bs=BeautifulSoup(r.text,"lxml")
    text=bs.select("body > div.gnt_cw_w > main > article > div.gnt_ar_b > p")
    
    content=[t.text for t in text]
    content = " ".join(content)
    contents+=content.lower()

# word_list=[word.replace('.','').replace(',','').replace('"','').split('\xa0')[0] for word in word_list if len(word)>3 and word.isalpha()]
word_list=re.findall(r'\b[a-z]{4,15}\b',contents)
word_list=list(set(word_list))


def quiz(word):
    try:
        url="https://ac.dict.naver.com/enkodict/ac?st=11001&q={}".format(word)
        r=requests.get(url)
        j=json.loads(r.text)
        _quiz=j["items"][0][0][1][0]
        print("*"*75,"\n\t"+_quiz+"\n"+"*"*75)
        return 1
    except:
        return 0
    
cnt=0
def raisehand(word):
    global cnt
    chance=5
    for i in range(chance):
        print("기회 : {}번".format(5-i))
        answer=input("답은 무엇일까요? > ")
        if answer==word:
            print("맞았습니다!!!")
            print("\n")
            cnt+=1
            return
        else:
            print("틀렸습니다\nhint : ",end='')
            for j in range(i):
                print(word[j],end=' ')
            for j in range(len(word)-i):
                print("_",end=' ')
            print('\n')
    print("답은 {}입니다".format(word))

for i in range(10):
    rnd=random.randint(0,len(word_list))
    if(quiz(word_list[rnd])):
        raisehand(word_list[rnd])
    del word_list[rnd]
print("10개중 {}개 맞았습니다".format(cnt))