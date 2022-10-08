def num(n):
    b = n * (1 / 3)
    if b != int(b):
        print(f"El numero {n} no es divisible por 3")
    else:
        print(f"El numero {n} es divisible por 3")
        return


num(3)
