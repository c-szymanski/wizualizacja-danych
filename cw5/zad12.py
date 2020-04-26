def miesiace():
    lista=['styczeń','luty','marzec','kwiecień','maj','czerwiec','lipiec',
                     'sierpień','wrzesień','październik','listopad','grudzień']
    for i in range(0, 12, 1):
        yield lista[i]

gen=miesiace()
for i in range(0, 12, 1):
    print(next(gen))