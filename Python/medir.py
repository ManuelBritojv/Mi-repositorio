arr_cm = ["cm", " cm", "centimetros", " centimetros", "centimetro", " centimetro"]
arr_m = ["m", " m", "metros", " metros", "metro", " metro"]
arr_km = ["km", " km", "kilometros", " kilometros", "kilometro", " kilometro"]

def isNumeric(n):
	try:
		float(n)
		return True
	except ValueError:
		return False

def otravez():
    n = input("¿Desea ejecutar el programa otra vez? si/no\n")
    n = n.lower()
    if n == "si" or n == " si":
        medir()
    if n == "no" or n == " no":
        quit()
    else:
        otravez()

def centimetros():
    n = input("¿Desea pasar de centimetros a metros o a kilometros? \n")
    n = n.lower()
    if n == arr_m[0] or n == arr_m[1] or n == arr_m[2] or n == arr_m[3] or n == arr_m[4] or n == arr_m[5]:
        cm_a_m()
    if n == arr_km[0] or n == arr_km[1] or n == arr_km[2] or n == arr_km[3] or n == arr_km[4] or n == arr_km[5]:
        cm_a_km()
    else:
        print("Valor ingresado no valido, intente otra vez\n")
        centimetros()

def cm_a_m():
    n = input("Ingrese centimetros que desea pasar a metros \n")
    if isNumeric(n) == True:
        n = float(n)
        c = n / 100
            
        if c == int(c):
            print(f"{n} centimetros son {int(c)} metros\n")
            otravez()
        else:
            print(f"{n} centimetros son {c} metros\n")
            otravez()
    if isNumeric(n) == False:
        print("Valor ingresado no valido, intente otra vez\n")
        cm_a_m()

def cm_a_km():
    n = input("Ingrese centimetros que desea pasar a kilometros \n")
    if isNumeric(n) == True:
        n = float(n)
        c = n / 100000

        if c == int(c):
            print(f"{n} centimetros son {int(c)} kilometros\n")
            otravez()
        else:
            print(f"{n} centimetros son {c} kilometros\n")
            otravez()
    if isNumeric(n) == False:
        print("Valor ingresado no valido, intente otra vez\n")
        cm_a_km()

def metros():
    n = input("¿Desea pasar de metros a centimetros o a kilometros? \n")
    n = n.lower()
    if n == arr_cm[0] or n == arr_cm[1] or n == arr_cm[2] or n == arr_cm[3] or n == arr_cm[4] or n == arr_cm[5]:
        m_a_cm() 
    if n == arr_km[0] or n == arr_km[1] or n == arr_km[2] or n == arr_km[3] or n == arr_km[4] or n == arr_km[5]:
        m_a_km()
    else:
        print("Valor ingresado no valido, intente otra vez\n")
        metros()

def m_a_cm():
    n = input("Ingrese metros que desea pasar a centimetros \n")
    if isNumeric(n) == True:
        n = float(n)
        c = n * 100

        if c == int(c):
            print(f"{n} metros son {int(c)} centimetros\n")
            otravez()
        else:
            print(f"{n} metros son {c} centimetros\n")
            otravez()
    if isNumeric(n) == False:
        print("Valor ingresado no valido, intente otra vez\n")
        m_a_cm()

def m_a_km():
    n = input("Ingrese metros que desea pasar a kilometros \n")
    if isNumeric(n) == True:
        n = float(n)
        c = n / 1000

        if c == int(c):
            print(f"{n} metros son {int(c)} kilometros\n")
            otravez()
        else:
            print(f"{n} metros son {c} kilometros\n")
            otravez()
    if isNumeric(n) == False:
        print("Valor ingresado no valido, intente otra vez\n")
        m_a_km()

def kilometros():
    n = input("¿Desea pasar de kilometros a metros o a centimetros? \n")
    n = n.lower()
    if n == arr_m[0] or n == arr_m[1] or n == arr_m[2] or n == arr_m[3] or n == arr_m[4] or n == arr_m[5]:
        km_a_m()
    if n == arr_cm[0] or n == arr_cm[1] or n == arr_cm[2] or n == arr_cm[3] or n == arr_cm[4] or n == arr_cm[5]:
        km_a_cm()
    else:
        print("Valor ingresado no valido, intente otra vez\n")
        kilometros()

def km_a_cm():
    n = input("Ingrese kilometros que desea pasar a centimetros \n")
    if isNumeric(n) == True:
        n = float(n)
        c = n * 100000

        if c == int(c):
            print(f"{n} kilometros son {int(c)} centimetros\n")
            otravez()
        else:
            print(f"{n} kilometros son {c} centimetros\n")
            otravez()
    if isNumeric(n) == False:
        print("Valor ingresado no valido, intente otra vez\n")
        km_a_cm()

def km_a_m():
    n = input("Ingrese kilometros que desea pasar a metros \n")
    if isNumeric(n) == True:
        n = float(n)
        c = n * 1000

        if c == int(c):
            print(f"{n} kilometros son {int(c)} metros\n")
            otravez()
        else:
            print(f"{n} kilometros son {c} metros\n")
            otravez()
    if isNumeric(n) == False:
        print("Valor ingresado no valido, intente otra vez\n")
        km_a_m()

def medir():
    n = input("¿Que medida desea transformar centimetros, metros, o kilometros? \n") 
    n = n.lower()
    if n == arr_cm[0] or n == arr_cm[1] or n == arr_cm[2] or n == arr_cm[3] or n == arr_cm[4] or n == arr_cm[5]:
        centimetros()
    if n == arr_m[0] or n == arr_m[1] or n == arr_m[2] or n == arr_m[3] or n == arr_m[4] or n == arr_m[5]:
        metros()
    if n == arr_km[0] or n == arr_km[1] or n == arr_km[2] or n == arr_km[3] or n == arr_km[4] or n == arr_km[5]:
        kilometros()
    else:
        print("Valor ingresado no valido, intente otra vez \n")
        medir()

medir()