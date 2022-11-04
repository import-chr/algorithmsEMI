# Cabo Cdtes. Christian Jair Loeza Ramirez

import heapq

lista3 = []
heapq.heapify(lista3)

print('lista inicial: ')
print(lista3)

for i in range(50):
    heapq.heappush(lista3, (i + 1))

print('lista llena: ')
print(lista3)

for i in range(len(lista3)):
    print(heapq.heappop(lista3))

print('lista vaciada: ')
print(lista3)