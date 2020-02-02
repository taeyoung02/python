# def outer_function(msg):
#     def inner_function():
#         return "inner : {}".format(msg)
#     return inner_function

# c= outer_function("hello")
# print(c())

import time
def time_chker(func):
    def inner_function(*args, **kwargs):
        start_time=time.time()
        result=func(*args,**kwargs) #test1() 실행값
        end_time=time.time()
        print("func:{}, time:{}".format(func.__name__,end_time-start_time))
        return result
    return inner_function #result리턴


def test1():
    for i in range(5):
        time.sleep(0.3)
        print("zzz")

@time_chker
def test2():
    for i in range(3):
        time.sleep(0.1)
        print("sleep")

time_chker(test1())
p=time_chker(test1)
p()
test2()