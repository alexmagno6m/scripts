#Day 29, not for me
def find_max_bitwise(n, k):
    max_bitwise = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            bitwise = i & j
            if max_bitwise < bitwise < k:
                max_bitwise = bitwise
                if max_bitwise == k - 1:
                    return max_bitwise

    return max_bitwise