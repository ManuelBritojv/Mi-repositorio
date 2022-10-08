def medir():
    n = input("¿Que medida desea transformar centimetros, metros, o kilometros?")
    if n == "centimetros" or n == " centimetros":
        n = input("¿Desea pasar de centimetros a metros o a kilometros?")
        if n == "metros" or n == " metros":
            n = input("Ingrese centimetros que desea pasar a metros")
            n = float(n)
            c = n / 100
            if c == int(c):
                print(f"{n} centimetros son {int(c)} metros")
            else:
                print(f"{n} centimetros son {c} metros")
        if n == "kilometros" or n == " kilometros":
            n = input("Ingrese centimetros que desea pasar a kilometros")
            n = float(n)
            c = n / 100000
            if c == int(c):
                print(f"{n} centimetros son {int(c)} kilometros")
            else:
                print(f"{n} centimetros son {c} kilometros")
    if n == "metros" or n == " metros":
        n = input("¿Desea pasar de metros a centimetros o a kilometros?")
        if n == "centimetros" or n == " centimetros":
            n = input("Ingrese metros que desea pasar a centimetros")
            n = float(n)
            c = n * 100
            if c == int(c):
                print(f"{n} metros son {int(c)} centimetros")
            else:
                print(f"{n} metros son {c} centimetros")
        if n == "kilometros" or n == " kilometros":
            n = input("Ingrese metros que desea pasar a kilometros")
            n = float(n)
            c = n / 1000
            if c == int(c):
                print(f"{n} metros son {int(c)} kilometros")
            else:
                print(f"{n} metros son {c} kilometros")
    if n == "kilometros" or n == " kilometros":
        n = input("¿Desea pasar de kilometros a metros o a centimetros?")
        if n == "metros" or n == " metros":
            n = input("Ingrese kilometros que desea pasar a metros")
            n = float(n)
            c = n * 1000
            if c == int(c):
                print(f"{n} kilometros son {int(c)} metros")
            else:
                print(f"{n} kilometros son {c} metros")
        if n == "centimetros" or n == " centimetros":
            n = input("Ingrese kilometros que desea pasar a centimetros")
            n = float(n)
            c = n * 100000
            if c == int(c):
                print(f"{n} kilometros son {int(c)} centimetros")
            else:
                print(f"{n} kilometros son {c} centimetros")


medir()
