class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    def __ge__(self,kwadrat2):
        if(self.x>=kwadrat2.x):
            return True
        else:
            return False
    def __gt__(self,kwadrat2):
        if(self.x>kwadrat2.x):
            return True
        else:
            return False
    def __le__(self,kwadrat2):
        if(self.x<=kwadrat2.x):
            return True
        else:
            return False
    def __lt__(self,kwadrat2):
        if(self.x<kwadrat2.x):
            return True
        else:
            return False

kw1=Kwadrat(2)
kw2=Kwadrat(2)
kw3=Kwadrat(4)
print('Kw1 ma bok długości: '+str(kw1.x))
print('Kw2 ma bok długości: '+str(kw2.x))
print('Kw3 ma bok długości: '+str(kw3.x))
print('__ge__:')
print('kw1 >= kw2:',kw1>=kw2)
print('kw1 >= kw3:',kw1>=kw3)
print('kw3 >= kw1:',kw3>=kw1)
print('__gt__:')
print('kw1 > kw2:',kw1 > kw2)
print('kw1 > kw3:',kw1 > kw3)
print('kw3 > kw1:',kw3 > kw1)
print('__le__:')
print('kw1 <= kw2:',kw1 <= kw2)
print('kw1 <= kw3:',kw1 <= kw3)
print('kw3 <= kw1:',kw3 <= kw1)
print('__lt__:')
print('kw1 < kw2:',kw1 < kw2)
print('kw1 < kw3:',kw1 < kw3)
print('kw3 < kw1:',kw3 < kw1)