a = (52+56+60)/3
agenda = {'juan':10, 'lina':2, 'maria':3, 'maria':4}
b = len(agenda)
a = 'HolA'
#comprobar si las letras estan en mayusculas o minusculas
for j in range(4):
    print(a[j].upper() in a)

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))
#comprobando en una cadena si alguna letra esta en mayusculas
filter_letter = list(filter(lambda i: i[0].upper() in a, a))
print(filter_letter)
string_return = list(map(lambda i: i[0].upper() in a, a))
print(string_return)
new_string = [a[i] for i in range(4) if string_return[i]==True]
print(new_string)
d = ''
for j in range(4):
    if string_return[j]==True:
       d = d + a[j]
    else:
        d = d + a[j]
#print(d)
b = 'Hello'
#print(b.swapcase())
#print(b)
c = b.lower()
#print(c)
#palindrromo
fon = 'A mi loca Colima'
r_for = fon.lower()
r_ready=r_for.replace(" ", "")
r_readyy=r_ready.replace(",", "")
print('oracion lista=',r_readyy)
fon_reverse = ''
l = len(r_readyy)
for j in range(l):
    fon_reverse = r_readyy[j] + fon_reverse
print('oracion inversa=',fon_reverse)
if r_readyy == fon_reverse:
    print('is palindromo')
else:
    print('no es palindromo')
#funciones recursivas
def factorial(num):
    if num >=2 and num<=12:
        num = num*factorial(num-1)
    return num

  
a = factorial(13)
print(a)