#Day 14 - 30 days of code, scope
class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        new_array = list(map(lambda x: abs(x), self.__elements))
        v_max = max(new_array)
        v_min = min(new_array)
        self.maximumDifference = v_max - v_min

mi_lista = Difference([-3,2,3])
mi_lista.computeDifference()
print(mi_lista.maximumDifference)