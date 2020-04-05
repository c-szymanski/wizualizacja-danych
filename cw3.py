#zad1
def zad1():
    A=[1/x for x in range(1,11,1)]
    B=[2**x for x in range(0,11,1)]
    C=[x for x in B if x%4==0]
    print(A)
    print(B)
    print(C)
#zad2
import random
def zad2():
    macierz=[[random.randint(0,9) for j in range(0,4,1)] for i in range(0,4,1)]
    przekatna=[macierz[i][j] for i in range(0,4,1) for j in range(0,4,1) if i==j]
    print('Macierz:')
    print(macierz[0])
    print(macierz[1])
    print(macierz[2])
    print(macierz[3])
    print('Przekatna:')
    print(przekatna)
#zad3
def zad3():
    slownik={
        'jablka': 'kg',
        'cola': 'butelki',
        'zelki': 'paczki'}
    nowy_slownik={value: key for key, value in slownik.items()}
    print('Stary slownik:')
    print(slownik)
    print('Nowy slownik:')
    print(nowy_slownik)
#zad4
def monotonicznosc(a):
    if(a>0):
        return 'funkcja rosnaca'
    if(a<0):
        return 'funkcja malejaca'
    if(a==0):
        return 'funkcja stala'

def zad4():
    print('y = ax + b')
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    print('Funkcja y = '+str(a)+'x + '+str(b)+' jest '+str(monotonicznosc(a)))
#zad5
def proste_czy_rownolegle(a1, a2):
    if(a1==a2):
        return 'równoległe'
    if(a1*a2==-1):
        return 'prostopadłe'
    else:
        return 'ani równoległe ani prostopadłe'

def zad5():
    print('y = ax + b')
    a1 = float(input('Podaj a1: '))
    b1 = float(input('Podaj b1: '))
    a2 = float(input('Podaj a2: '))
    b2 = float(input('Podaj b2: '))
    print('y1 = '+str(a1)+'x + '+str(b1))
    print('y2 = '+str(a2)+'x + '+str(b2))
    print('Proste y1 i y2 są '+str(proste_czy_rownolegle(a1, a2)))

#zad6
def okrag(a = 0, b = 0, x = 0, y = 0):
    return ((x-a)**2 + (y-b)**2)**0.5

def zad6():
    a = input('Podaj wspolrzędna a: ')
    b = input('Podaj wspolrzedna b: ')
    x = input('Podaj wspolrzedna x: ')
    y = input('Podaj wspolrzedna y: ')
    print('Promien okregu ma dlugosc rowna:',okrag(float(a), float(b), float(x), float(y)))

#zad7
def pitagoras(a=2,b=4):
    return(a**2+b**2)**0.5
def zad7():
    a=float(input('Podaj a: '))
    b=float(input('Podaj b: '))
    print('Dlugosc przeciwprostokatnej to:',pitagoras(a,b))

#zad8
def suma_ciagu(a1=1,r=1,ile=10):
    return ile*((2*a1)+(ile-1)*r)/2

def zad8():
    a1=float(input('Podaj a1: '))
    r=float(input('Podaj r: '))
    ile=int(input('Podaj ile: '))
    print('suma = ',str(suma_ciagu(a1, r, ile)))
#zad9
def iloczyn_ciagu(* liczby):
    if(len(liczby)==0):
        return 0.0
    else:
        iloczyn=1
        for i in liczby:
            iloczyn = iloczyn * i
        return iloczyn

def zad9():
    print('iloczyn dla ciągu bez elementów:', iloczyn_ciagu())
    print('iloczyn dla ciągu 1,2,3,7,9:', iloczyn_ciagu(1,2,3,7,9))  

#zad10

def ilosc_produnktow(**lista_zakupow):
    suma = 0
    for i in lista_zakupow:
        suma = suma + float(lista_zakupow[i])
    return suma

def zad10():
    print('liczba wszystkich produktów:', ilosc_produnktow(jablko=2,banan=5,
          dlugopis=6, zeszyt=3, koszulka=1))

zad10()