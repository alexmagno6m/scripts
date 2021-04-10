# day 19 - interfaces python
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        self.div = [j for j in range(1, n + 1) if n % j == 0]
        return sum(self.div)


my_calculator = Calculator()
s = my_calculator.divisorSum(6)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
