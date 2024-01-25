a=8
b=0

try:
    print(c/b)
except ZeroDivisionError:
    print("error no se puede dividir entres 0")
except NameError:
    print("La variable no existe")
except:
    print("Algo salio mal")




