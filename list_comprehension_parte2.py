a = [2,1,3]
b = [2,4,6]
total = []
for i in range(3):
    total.append(a[i]*b[i])
print(total)
nueva_lista = [a[i]*b[i] for i in range(3)]
print(nueva_lista)
a = 1 
b = 12
if (a and b) >= 0 and (a and b) <= 11:
    print(a+b)

n = 3
names = []
scores = []

for i in range(n):
    name = str(input('nombre'))
    score = float(input('puntaje'))
    names.append(name)
    scores.append(score)
    
print(names)
for j in range (10):
    print(j)