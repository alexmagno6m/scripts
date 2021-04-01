#imprimir en un binario la mayor agrupacion de numeros 1s, dado un numero n
n = 124567
b = bin(n)
# 1 se necesita desde la posicion 2, ya que los dos primeros valores indican el tipo
b = b[2:]
# 2 se divide el numero por los ceros que se tengan para crear grupos de unos
array = b.split('0')
# 3 usando list comprehension se genera un arreglo con la longitud de cada grupo de 1
otro = [len(array[i]) for i in range(len(array))]
#4 se imprime el elemento de mayor valor en este arreglo
print(max(otro))
#* en esta forma alternativa evitamos el paso
print(len(max(array)))
# hello 