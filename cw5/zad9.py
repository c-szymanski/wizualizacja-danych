def generator(dane):
    for i in range(0, len(dane), 2):
        yield dane[i]

liczby=generator([0,1,2,3,4,5,6,7])
print(next(liczby),end=', ')
print(next(liczby),end=', ')
print(next(liczby),end=', ')
print(next(liczby))