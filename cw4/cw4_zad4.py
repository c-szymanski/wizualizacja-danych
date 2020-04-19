class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl_produkt(self):
        print('nazwa produktu: '+self.nazwa_produktu)
        print('ilosc: '+str(self.ilosc))
        print('jednostka miary: '+self.jednostka_miary)
        print('cena jed: '+str(self.cena_jed))
    def ile_produktu(self):
        return (str(self.ilosc)+' '+self.jednostka_miary)
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed
obiekt=NaZakupy('Ananas',4,'szt',8.99)
obiekt.wyswietl_produkt()
print(obiekt.ile_produktu())
print(obiekt.ile_kosztuje())


