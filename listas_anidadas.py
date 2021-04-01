numeros = [2,2,3,4,3,4,1]
numeros.sort()
print(numeros)

i=1
j=1
e=len(numeros)
match= 0
value=0
while i < e:
    if numeros[i]>numeros[0]:
        match=i
        value=numeros[i]
        break
    else:
        i+=1
print('match=',match)
print('value=', value)
while match<e:
    if numeros[match]==value:
        print(numeros[match])
        match+=1
    else:
        break
