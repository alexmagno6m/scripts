# Day 18 - hackerRank - palindrome
class Solution():
    def __init__(self, stack='', queue=''):
        self.stack = stack
        self.queue = queue

    def pushCharacter(self, nuevas):
        self.stack = self.stack + nuevas

    def enqueueCharacter(self, nuevas):
        self.queue = nuevas + self.queue

    def popCharacter(self):
        return self.stack

    def dequeueCharacter(self):
        return self.queue


s = 'tacocat'
obj = Solution()
l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")

# fon = 'racecar'
# r_for = fon.lower()
# r_ready=r_for.replace(" ", "")
# r_readyy=r_ready.replace(",", "")
# print('oracion lista=',r_readyy)
# fon_reverse = ''
# l = len(r_readyy)
# for j in range(l):
#     fon_reverse = r_readyy[j] + fon_reverse
# print('oracion inversa=',fon_reverse)
# if r_readyy == fon_reverse:
#     print('is palindromo')
# else:
#     print('no es palindromo')
