from collections import Counter
numbers = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
b = Counter(numbers)
print(b.items())
# sale = [6, 6, 6, 4, 18, 10]
# stock = list(filter(lambda x: x > 5, numbers))
# stock2 = [numbers[x]*2 for x in range(10) if numbers[x] > 5]
# print(stock2)
# stock3 = list(filter(lambda x: x > 5, numbers))
# print(stock3)

# e = {2: 2}
# b.subtract(e)
# item = 4
# price = 50
total = 0
items = [6, 6, 6, 4, 18, 10]
prices = [55, 45, 55, 40, 60, 50]
for i in range(6):
    if b[items[i]] > 0:
        total = prices[i] + total
        e = {items[i]: 1}
        b.subtract(e)

print(total)
print(b.items())
