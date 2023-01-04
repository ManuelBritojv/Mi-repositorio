import barcode
from barcode.writer import ImageWriter
from barcode import EAN13

def codigos():
    global lista
    lista=[]

    for index in range(1,10):
        if len(str(index))<2:
            lista.append(str(index) + "00000000000")
        elif len(str(index))<3:
            lista.append(str(index) + "0000000000")
        elif len(str(index))<4:
            lista.append(str(index) + "000000000")
        elif len(str(index))<5:
            lista.append(str(index) + "00000000")
        elif len(str(index))<6:
            lista.append(str(index) + "0000000")
        elif len(str(index))<7:
            lista.append(str(index) + "000000")
        elif len(str(index))<8:
            lista.append(str(index) + "00000")
        elif len(str(index))<9:
            lista.append(str(index) + "0000")
        elif len(str(index))<10:
            lista.append(str(index) + "000")
        elif len(str(index))<11:
            lista.append(str(index) + "00")
        elif len(str(index))<12:
            lista.append(str(index) + "0")
    
    return lista

def generar_codigos():
    lista_numeros = []
    numeros = codigos()
    for item in numeros:
        with open("imagenes/imagen"+ str(item)+".jpeg","wb") as fichero:
            EAN13.write(str(item),writer=ImageWriter()).write(fichero)

generar_codigos()