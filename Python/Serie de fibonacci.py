def fib(d):
    a = 0
    b = 1
    c = 1
    while c <= d:
        print(a)
        a = a + b
        b = a - b
        c = c + 1
    else:
        return


fib(10)
