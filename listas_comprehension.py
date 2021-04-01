x = [0,1]
y = [0,1]
z = [0,1,2]
matrix = [x, y, z]
#print(matrix)
newList=[]
otherList = []
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(z)):
            newList.append([x[i], y[j], z[k]])
            if x[i] + y[j] + z[k] !=3:
                otherList.append([x[i], y[j], z[k]])

print(newList)
print(otherList)
"""
otherList=[]
otherList.append([x[0], y[0], z[0]])
otherList.append([x[0], y[0], z[1]])
otherList.append([x[0], y[0], z[2]])
otherList.append([x[0], y[1], z[0]])
otherList.append([x[0], y[1], z[1]])
otherList.append([x[0], y[1], z[2]])
otherList.append([x[1], y[0], z[0]])
otherList.append([x[1], y[0], z[1]])
otherList.append([x[1], y[0], z[2]])
otherList.append([x[1], y[1], z[0]])
otherList.append([x[1], y[1], z[1]])
otherList.append([x[1], y[1], z[2]])
print(otherList)
"""
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[p] for row in matrix] for p in range(2)]
print (transpose)
#new_matrix = [list([i for [j for [k for k in z]in y]in x])]
#new_matrix= [[[x[i] for i in range(x)] for y[i] in range(y)] for z[i] in range(z)]
print(newList[0])
listaNueva = [[i,j,k] for i in x for j in y for k in z]
listaNueva2 = [[i, j, k] for i in x for j in y for k in z if i+j+k != 3]
print(listaNueva)
print(listaNueva2)
x = 1
y = 2
z = 3
n = 3
x = [item for item in range(x+1)]
y = [item for item in range(y+1)]
z = [item for item in range(z+1)]
print(x)
print(y)
print(z)
newList = [[i,j,k]for i in x for j in y for k in z if i+j+k != n]
print(newList)