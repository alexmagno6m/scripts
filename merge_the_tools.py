def merge_the_tools(string, k):
    l=[]
    m=0
    for i in range(len(string)//k):
        l.append(string[m:m+k])
        m+=k
    print(l)
    for v in l:
        print(''.join(list(dict.fromkeys(list(v)).keys())))
a = ['aaa', 'bca', 'dda']
'''
el metodo keys funciona porque devuelve todas las claves,
de un diccionario, sin repetir. Por lo tanto,
en el primer elemento de la lista 'aaa', la clave es a.
'''
print(''.join(dict.fromkeys(a[0]).keys()))
b = {'hola':2, 'hola':3, 'nombre':'alex'}
print(b.keys())