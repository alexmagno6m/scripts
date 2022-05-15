from collections import Counter
numbers = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
b = Counter(numbers).items()
print(b)
sale = [6, 6, 6, 4, 18, 10]
stock = list(filter(lambda x: x > 5, numbers))
stock2 = [numbers[x]*2 for x in range(10) if numbers[x] > 5]
print(stock2)
stock3 = list(filter(lambda x: x > 5, numbers))
print(stock3)