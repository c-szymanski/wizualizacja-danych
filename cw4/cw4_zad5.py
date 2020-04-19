class ciag_aryt:
    def __init__(self,a1,roznica,dlugosc):
        self.a1=a1
        self.roznica=roznica
        self.dlugosc=dlugosc
    def wyswietl_dane(self):
        print('a1='+str(self.a1))
        print('roznica='+str(self.roznica))
        print('dlugosc='+str(self.dlugosc))
    def pobierz_parametry(self,a1,roznica,dlugosc):
        self.a1=a1
        self.roznica=roznica
        self.dlugosc=dlugosc
    def policz_sume(self):
        an=self.a1+(self.dlugosc-1)*self.roznica
        suma=(self.a1+an)/2*self.dlugosc
        return str(suma)

obiekt=ciag_aryt(0,2,10)
obiekt.wyswietl_dane()
print('nowy ciag:')
obiekt.pobierz_parametry(1,2,2)
obiekt.wyswietl_dane()
print('suma: '+obiekt.policz_sume())