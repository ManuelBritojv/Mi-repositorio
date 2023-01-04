def medir():
    n = input("¿Que medida desea transformar centimetros, metros, o kilometros?")
    if n != "centimetros":
        if n != "metros":
            if n != "kilometros":
                print("Error respuesta ilogica")
                return()
            else:
                n = input("¿Desea pasar de kilometros a centimetros o a metros?")
                if n != "centimetros":
                    if n != "metros":
                        print("Error respuesta ilogica")
                    else:
                        n = input("Ingrese kilometros que desea pasar a metros")
                        n = float(n)
                        c = n * 1000
                        if c == int(c):
                            print(f"{n} kilometros son {int(c)} metros")
                        else:
                            print(f"{n} kilometros son {c} metros")
                else:
                    n = input("Ingrese kilometros que desea pasar a centimetros")
                    n = float(n)
                    c = n * 100000
                    if c == int(c):
                        print(f"{n} kilometros son {int(c)} centimetros")
                    else:
                        print(f"{n} kilometros son {c} centimetros")
        else:
            n = input("¿Desea pasar de metros a centimetros o a kilometros?")
            if n != "centimetros":
                if n != "kilometros":
                    print("Error respuesta ilogica")
                else:
                    n = input("Ingrese metros que desea pasar a kilometros")
                    n = float(n)
                    c = n / 1000
                    if c == int(c):
                        print(f"{n} metros son {int(c)} kilometros")
                    else:
                        print(f"{n} metros son {c} kilometros")
            else:
                n = input("Ingrese metros que desea pasar a centimetros")
                n = float(n)
                c = n * 100
                if c == int(c):
                    print(f"{n} metros son {int(c)} centimetros")
                else:
                    print(f"{n} metros son {c} centimetros")
    else:
        n = input("¿Desea pasar de centimetros a metros o a kilometros?")
        if n != "metros":
            if n != "kilometros":
                print("Error respuesta ilogica")
                return()
            else:
                n = input("Ingrese centimetros que desea pasar a kilometros")
                n = float(n)
                c = n / 100000
                if c == int(c):
                    print(f"{n} centimetros son {int(c)} kilometros")
                else:
                    print(f"{n} centimetros son {c} kilometros")   
        else:
            n = input("Ingrese centimetros que desea pasar a metros")
            n = float(n)
            c = n / 100
            if c == int(c):
                print(f"{n} centimetros son {int(c)} metros")
            elif c != int(c):
                print(f"{n} centimetros son {c} kilometros")

        

medir()