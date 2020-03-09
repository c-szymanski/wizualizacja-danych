#zadanie1
def zadanie1():
    a = input("podaj napis:")
    print(a)
    print('spacja powtarza sie', a.count(' '), 'razy')
#zadanie2
def zadanie2():
    import sys
    print('podaj liczbe 1')
    a=sys.stdin.readline()
    print('liczba1 to: '+a)
    print('podaj liczbe 2')
    b=sys.stdin.readline()
    print('liczba2 to: '+b)
    a=int(a)
    b=int(b)
    c=a*b
    c=str(c)
    sys.stdout.write(c)
#zadanie4
def zadanie4():
    a=input('Podaj liczbe:')
    a=int(a)
    if a>=0:
        print('Wartosc bezwzgledna z tej liczby to:',a)
    else:
        a=a*-1
        print('Wartosc bezwzgledna z tej liczby to:',a)
#zadanie5
def zadanie5():
    a=input('podaj liczbe1:')
    b=input('podaj liczbe2:')
    c=input('podaj liczbe3:')
    a,b,c=int(a),int(b),int(c)
    if a>=0 and a<=10 and(a>b or b>c):
        print('gituwa')
    else: 
        print('warunki nie spelnione')
#zadanie6
def zadanie6():
    lista=[25,1,2,3,5,10,15,20]
    lista.sort()
    for x in lista:
        if x%5==0:
            print(str(x))
#zadanie 7
def zadanie7():
    lista=[]
    for licznik in range(1,6,1):
        liczba=input('podaj '+str(licznik)+' liczbe: ')
        lista.append(int(liczba))
    for licznik in range (0,5,1):
        print(str(lista[licznik])+'^2='+str(lista[licznik]**2))
#zadanie 8
def zadanie8():
    lista=[]
    licznik=0
    while licznik<5:
        liczba=input('Podaj liczbe: ')
        lista.append(int(liczba))
        licznik=licznik+1
    print(lista)
zadanie8()