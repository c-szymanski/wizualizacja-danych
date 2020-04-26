class iterator:
    def __init__(self,data):
        self.data=data
        self.index=-2
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            raise StopIteration
        self.index+=2
        return self.data[self.index]
liczby=iterator([0,1,2,3,4,5,6,7])
print(next(liczby),end=', ')
print(next(liczby),end=', ')
print(next(liczby),end=', ')
print(next(liczby))