#========================================#
#                                        #
#Cabo Cdtes. Christian Jair Loeza Ramirez#
#                                        #
#========================================#

apellido = "LOEZA"

for i in range(len(apellido)):
    print(ord(apellido[i]))

name = input("Nombre: ")
suma = 0

print(name)

for i in range(len(name)):
    print(ord(name[i]))

    suma += ord(name[i])

print(f'suma: {suma}')


