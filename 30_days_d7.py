n = int(input())
if n>=1 and n<= 1000:
    arr = map(int, input().rstrip().split())
    lista = list(arr)
    #para evitar realizar un nuevo loop, creo un filtro de los valores de la condicion
    #si hay datos fuera del rango la nueva lista tendra una dimension menor, por lo que 
    #no coincidira con la lista original.
    lista_final = list(filter(lambda x: x>=1 and x<=10000, lista))
    b = len(lista_final)
    if len(lista)==n and len(lista)==b:
        txt = ''
        for i in range(b):
            txt = str(lista[i]) + ' ' + txt
        print(txt)
    else:
        pass


#lista_f = [item for item in lista if (item >= 1) and (item <= 10000)]
#print(lista_f)
