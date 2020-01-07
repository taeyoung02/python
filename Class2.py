class override:
    def __init__(self,*args):
        self.arr=[args[i] for i in range(len(args))]
    def add(self):
        sum=0
        for i in range(len(self.arr)):
            sum+=self.arr[i]
        return sum
instance=override(1,2,3,4)
print(instance.add())

class over2(override):
    def add2(self):
        sum=0
        for i in range(len(self.arr)):
            sum+=self.arr[i]
        return sum
instance.arr.append(3)
print(instance.arr)