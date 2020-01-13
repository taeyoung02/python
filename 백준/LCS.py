a=input("")
b=input("")
lcs=[[0 for col in range(1001)] for row in range(1001)]
a=" "+a
b=" "+b
for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i]==b[j]:
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i-1][j], lcs[i][j-1])+(a[i]==b[j])
print(lcs[i][j])
        

        