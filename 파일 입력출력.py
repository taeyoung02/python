# file = open("C://python//test.txt", mode="w", encoding="utf-8") #(경로, 모드, 인코딩)
# file.write("taeyoungzzang")
# file.close()

rfile = open("test.txt","r",encoding="utf-8")
content = rfile.read(30) #30 까지 읽고 읽었으면 담을공간필요
print(content)

print(rfile.tell())#포인터의 위치 = 30
rfile.seek(0) #파일포인터를 맨처음으로
content=rfile.read() #모두 읽음
print(content)
# content=rfile.readline()
# print(content)

for l in rfile: #한줄씩 모두 출력
    print(l)
rfile.close()

print(content)

with open("test.txt",mode="r",encoding="utf-8")as taeyoung: #파일을 닫을필요없고 파일을 as뒤의 변수에 저장
    print(taeyoung.read())

# 문장마지막 역슬래쉬로 줄바꿈 가능
with open("test2.txt",mode="w",encoding='utf=8') as sex, \  
    open("test.txt", mode = "r", encoding='utf-8') as tape:
    sex.write(tape.read().replace("taeyoungzzang","태영짱")) #새 파일에 원래파일을 읽어서 씀
     