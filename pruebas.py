a = ['logan', 'volverine']
new_list = [elemento for elemento in a if len(elemento)<6]
print(new_list)
b = int(input())
lista = []
for i in range(b):
    item = int(input())
    lista.append(item)
lista2 = [item for item in lista if item>20]
print(lista)
print(lista2)
for i in range(10, -1, -1):
    print(i)