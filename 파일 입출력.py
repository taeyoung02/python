f=open('C:/Users/User/AppData/Local/Programs/Python/Python37-32/lib/site-packages/textfile.txt','w')
f.write('HELLO PYTHON') #내용을 바꿀수있다
f.close()

f=open('C:/Users/User/AppData/Local/Programs/Python/Python37-32/lib/site-packages/textfile.txt','r')
print('f.read() : {0}'. format(f.read())) #파일을 읽어옴
f.close()

#내용을 계속 추가
f=open('C:/Users/User/AppData/Local/Programs/Python/Python37-32/lib/site-packages/textfile.txt','a')
f.write('HELLO PYTHON') 
f.close()
#with ~ as 닫을필요없음
with open('C:/Users/User/AppData/Local/Programs/Python/Python37-32/lib/site-packages/textfile.txt','r')as f:
          print('f.read() : {0}'.format(f.read()))

ts = ['hello python\n', 'hello c++\n', 'hello java\n']

with open('C:/Users/User/AppData/Local/Programs/Python/Python37-32/lib/site-packages/textfile.txt','w')as f:
    #or f.writelines(ts) #리스트문자열 쓰기
     for tl in ts:
        f.write(tl)


with open('C:/Users/User/AppData/Local/Programs/Python/Python37-32/lib/site-packages/textfile.txt','r')as f:
    ls=f.readlines()#모든 문자열읽기
    print('type(ls) : {0}'. format(type(ls)))

    l=''
    for l in ls:
        print(l)
    
with open('C:/Users/User/AppData/Local/Programs/Python/Python37-32/lib/site-packages/textfile.txt','r')as f:
    l=f.readline()
    print('type(l) : {0}'. format(type(l)))

    c=1
    while l != '':
        print(l,end='') #프린트안에서 자체적으로 개행을 시키는데 개행문자를 ''로 바꿔줌
        l=f.readline() #행 단위로 문자열 읽기
        c+=1

    print('c-1 : {0}'.format(c-1))
