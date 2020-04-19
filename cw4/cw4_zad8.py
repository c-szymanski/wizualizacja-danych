class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ile_krokow):
        self.y=self.y+(self.krok*ile_krokow)
    def idz_w_dol(self,ile_krokow):
        self.y=self.y-(self.krok*ile_krokow)
    def idz_w_lewo(self,ile_krokow):
        self.x=self.x-(self.krok*ile_krokow)
    def idz_w_prawo(self,ile_krokow):
        self.x=self.x+(self.krok*ile_krokow)
    def pokaz_gdzie_jestes(self):
        print('aktualne wspolrzedne:')
        print('x='+str(self.x))
        print('y='+str(self.y))
    def __del__(self):
        print('Objekt zniszczony')

obiekt=Robaczek(0,0,1)
obiekt.pokaz_gdzie_jestes()
obiekt.idz_w_gore(1)
obiekt.pokaz_gdzie_jestes()
obiekt.idz_w_dol(2)
obiekt.pokaz_gdzie_jestes()
obiekt.idz_w_lewo(5)
obiekt.pokaz_gdzie_jestes()
obiekt.idz_w_prawo(4)
obiekt.pokaz_gdzie_jestes()
del obiekt