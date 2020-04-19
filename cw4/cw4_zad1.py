plik=open('zad1.txt','w')
for i in range (4,100,4):
    plik.write(str(i)+'\n')
plik.close()