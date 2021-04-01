#Day 11, 30 days of code
arr=[[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
test = [arr[i][j] for i in range(6) for j in range(6)
if (arr[i][j]>=-9 and arr[i][j]<=9)]
if len(test)==36:
    list_final = [sum(arr[i][j:j+3]+arr[i+2][j:j+3])
    +arr[i+1][j+1]for i in range(4) for j in range(4)]
    print(max(list_final))
else:
    pass
