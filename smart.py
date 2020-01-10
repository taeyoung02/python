import os

def calculator(func):
    operator=['+','-','*','/','=']
    def inner(*args, **kwargs):
        user_input=func(*args, **kwargs)
        if user_input==None:
            exit()
        string_list=[]
        lop=0

        for i, s in enumerate(user_input):
            if s in operator:
                if user_input[lop:i].strip()!="":
                    string_list.append(user_input[lop:i])
                    string_list.append(s)
                    lop = i+1
        string_list.append(user_input[lop:])


        pos=0
        while len(string_list)!=1:
            if string_list[pos] in operator:
                string_list.insert(0,str(eval(string_list[pos-1]+string_list[pos]+string_list[pos+1])))
                del string_list[pos:pos+3]
            else: 
                pos+=1

        print(string_list[0])
        return user_input
    return inner


def inputdata():
    user_input=input("input the formular>")
    if user_input=="exit":
        return None
    else:
        return user_input
    
start=calculator(inputdata)
while True:
    os.system("cls")
    start()
    os.system("pause")