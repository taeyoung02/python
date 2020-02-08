import time

def time_chker(func):
    def inner_function(*args, **kwargs):
        start_time=time.time()
        result=func(*args,**kwargs) #test1() 실행값
        end_time=time.time()
        print("func:{}, time:{}".format(func.__name__,end_time-start_time))
        return result
    return inner_function #result리턴