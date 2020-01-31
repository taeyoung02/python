Str=input()
status=0
stack=[]

for i in range(len(Str)):
    if Str[i]=="<":
        if status==0:
            while stack:
                print(stack.pop(),end='')
        print("<",end='')
        status+=1
    elif Str[i]==">":
        print(">",end='')
        status-=1
    elif status==0:
        if Str[i]==' ':
            while stack:
                print(stack.pop(),end='')
            print(' ',end='')
        else:
            stack.append(Str[i])
    else: print(Str[i],end='')
while stack:
    print(stack.pop(),end='')
