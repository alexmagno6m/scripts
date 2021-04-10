# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swap = 0
if n>=2 and n<=600:
    for i in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i+1]<a[i]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swap += 1


    print("Array is sorted in",swap, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[n-1])