with open("zad3.txt", "w") as plik:
    for i in range(0,11,1):
        plik.write(str(i)+'\n')
with open("zad3.txt", "r") as plik:
    for i in plik:
        print(i, end="")