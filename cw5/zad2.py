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
    def __add__(self, kwadrat2):
        return self.x+kwadrat2.x

kw1=Kwadrat(1)
kw2=Kwadrat(2)
kw3=Kwadrat(kw1+kw2)
kw4=Kwadrat(kw3+kw3)
print('Wymiary kwadratu 1:',kw1.x,'na',kw1.y)
print('Wymiary kwadratu 2:',kw2.x,'na',kw2.y)
print('Wymiary kwadratu 3:',kw3.x,'na',kw3.y)
print('Wymiary kwadratu 4:',kw4.x,'na',kw4.y)