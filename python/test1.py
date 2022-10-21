cad = input("cadena: ")

def getHash(cad):
    lencad = len(cad)
    suma = 0
    total = 0

    for i in range(lencad):
        suma += cad[i]

    total = sum % lencad

    return total


print(getHash(cad))