# Reto del dia Let's Review - 30 days of code
T = int(input())
if T >= 1 and T <= 10:
    strings = []
    for i in range(T):
        S = str(input())
        L = len(S)
        if L >=2 and L <= 10000:
            strings.append(S)    
    b = len(strings)
    for i in range(b):
        S = strings[i]
        L = len(S)
        nuevo =''
        for a in range(0,L,2):
            nuevo=nuevo + S[a]
        nuevo = nuevo + ' '
        for a in range(1,L,2):
            nuevo=nuevo + S[a]
        print(nuevo)
        
    

