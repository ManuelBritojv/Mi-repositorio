def pot(n):
    b = n / 2
    if b != int(b):
        a = n * n * n
        print(f"el cubo de {n} es {a}")
    else:
        a = n * n
        print(f"el cuadrado de {n} es {a}")
        return


pot(8)
