import random
import numpy
lotto=[]
def make_lotto_number(**kwargs):#dictionary 받음
    rand_number=numpy.random.choice(range(1,46),6,replace=False)#1부터46까지 랜덤수중에 6개를 중복없이 골라라
    rand_number.sort()

    lotto=[]
    if kwargs.get("include"):
        include=kwargs.get("include")
        lotto.extend(include)#kwargs.get이 리스트를 반환하는데 append를 하면 리스트가 더 붙으니 extend로 확장시킴
    
    cnt_make=6-len(lotto)

    if kwargs.get("exclude"):
        exclude=kwargs.get("exclude")
        lotto.extend(exclude)

    for _ in range(cnt_make):
        for j in rand_number:
            if lotto.count(j)==0:#lotto의 j값을 가진 요소갯수 반환
                lotto.append(j)
                break
    
    if kwargs.get("exclude"):
        lotto = list(set(lotto)-set(exclude))

    lotto.sort()
    return lotto

print(make_lotto_number(exclude=[3,4],include=[1,2]))