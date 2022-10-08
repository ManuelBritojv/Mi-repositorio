def prim(n):
    a = 2
    if n == 1 or n == 2:
        print(f"El número {n} es primo")
        return
    while a != n:
        b = n / a
        if b != int(b):
            a = a + 1
            if a == n:
                print(f"El número {n} es primo")
                return
        else:
            print(f"El número {n} no es primo")
            return
    else:
        return


prim(2)
