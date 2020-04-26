class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1=Point(0,0)
p2=Point(1,1)
p3=Point(20,20)

print(p1.counter)
print(p2.counter)
print(p3.counter)
p1.update(0)
p2.update(1)
p3.update(20)
p1.update(0)
print(p1.counter)
print(p2.counter)
print(p3.counter)
p1.counter.append('append')
print(p1.counter)
print(p2.counter)
print(p3.counter)