class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        print('nazwa:'+self.rodzaj)
class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo):
        self.rozmiar=rozmiar
        self.kolor=kolor
        self.dla_kogo=dla_kogo
    def wyswietl_dane(self):
        print('rozmiar:'+self.rozmiar)
        print('kolor:'+self.kolor)
        print('dla_kogo:'+self.dla_kogo)
class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.rodzaj_swetra=rodzaj_swetra
    def wyswietl_dane(self):
        print('rodzaj_swetra:'+self.rodzaj_swetra)
bawelna=Material('bawelna',1,2)
kaszmir=Material('kaszmir',3,4)
bawelna.wyswietl_nazwe()
kaszmir.wyswietl_nazwe()
ubranie1=Ubrania('M','zielony','Magda')
ubranie2=Ubrania('L','niebieski','Czarek')
ubranie1.wyswietl_dane()
ubranie2.wyswietl_dane()
sweter1=Sweter('Wkladany przez glowe')
sweter2=Sweter('Rozpinany')
sweter1.wyswietl_dane()
sweter2.wyswietl_dane()
