n = int(input())
student_marks = {}
if n>=2 and n<=10:
    bad = 0
    for j in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        a = [float(item)for item in line[1:]]
        #se crea una lista con los valores de la condicion, si no se cumple, la cantidad de items
        #sera diferente.
        b = [item for item in a if (item>=0 and item<=100)]
        #print(b)
        lenA = len(a)
        lenB = len(b)
        if lenA==3 and lenB==3:
            student_marks[name]=scores
            bad += 1
        else:
            bad = 0
        #print(bad)
    if bad == n:
        query_name = input()
        res = student_marks.get(query_name)
        l = len(res)
        total = 0
        num = 0
        for i in range(l):
            num = float(res[i]) + num
        promedio = num/l
        #para imprimir siempre dos decimales, el metodo round si el valor es exacto
        #solo muestra un cero.
        print('{:.2f}'.format(promedio))
    else:
        pass
else:
    pass
