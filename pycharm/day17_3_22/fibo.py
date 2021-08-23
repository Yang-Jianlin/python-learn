def fibo(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a+b
        n += 1


f = fibo(6)
for n in f:
    print(n)
