try:
    file=open("test.txt","r")
    n="10.5"
    v=int(n)
except Exception as e: #예외사항을 e에 저장
    print("error : {}".format(e)) #어떤 예외인지 알수있음
finally: #무조건 실행됨
    file.close()
    print("implemented")