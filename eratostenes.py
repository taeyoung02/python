#에라토스테네스의 체
import math
def eratostenes(num):
    prime=[]
    prime_check=[False, False]+[True]*(num-1)

    for i in range(2, int(math.sqrt(num)+1)):
        if prime_check[i]:
            for j in range(2*i,num+1, i):
                prime_check[j]=False
#comprehension
    prime=[i for i in range(2,num+1) if prime_check[i]]

    if num in prime : print(num,"is prime") 
    else : print(num,"is not prime")