def fib():
    a=0
    b=1
    while a>-1:
        b+=a
        a=b-a
        yield b-a

ciag=fib()
for i in range(0, 9, 1):
    print('ciag('+str(i)+')=',next(ciag))