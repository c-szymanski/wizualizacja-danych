class samogloski:
    def __init__(self,napis):
        if isinstance(napis,str):
            self.napis=napis
            self.index=0
            self.samogloski=['a','e','y','i','o','ą','ę','u','ó']
        else:
            raise ValueError('Typ danych inny niz string')
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.napis):
            raise StopIteration
        while self.index<len(self.napis):
            if self.napis[self.index] in self.samogloski:
                self.index+=1
                return self.napis[self.index-1]
            self.index+=1
napis=samogloski('abcdąz')
print('samogloski:')
print(next(napis),end=', ')
print(next(napis))