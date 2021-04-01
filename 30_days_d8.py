agenda = {}
n = int(input('ingrese datos'))
if n>=1 and n<=10**5:
    for i in range(n):
        data = input().split()
        name, phone = data[0], data[1]
        agenda[name]=phone
    #query = int(input('ingrese cantidad de consultas'))
    queryL = []
    if n >=1 and n<=10**5:
        for i in range(n):
            queryN = str(input('ingrese nombre'))
            queryL.append(queryN)
        l = len(queryL)
        for j in range(l):
            if agenda.get(queryL[j]):
                print('{}={}'.format(queryL[j], agenda.get(queryL[j])))
            else:
                print('Not found')
    else:
        pass
else:
    pass

