#Day 12 30 days of code
class Person(object):
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores= scores

    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        grades = [40, 55, 70, 80, 90, 101]
        letter = ['T', 'D', 'P', 'A', 'E', 'O']
        note = 0
        for i in range(6):
            if average < grades[i]:
                note = i
                break
        return letter[note]

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
'''
Esta version es para e 
const = input().split()
number = int(input())
scores = input().split()
final_scores = [int(x) for x in scores]
final_scores = list(filter(lambda x: x>=1 and x<=100,final_scores))
l = []
for i in range(3):
    l.append(len(const[i]))
if l[0]>=1 and l[1]>=1 and l[0]<=10 and l[1]<=10 and l[2]==7 and len(final_scores)==number:
    student1= student(const[0], const[1], const[2], final_scores)
    student1.printPerson()
    student1.calculate()
    print("Grade:", student1.calculate())
'''