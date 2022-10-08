def div(n):
    b = n / 6
    if b != int(b):
        print(f"El numero {n} no es divisible por 6")
    else:
        print(f"El numero {n} es divisible por 6")
        return


div(24)
