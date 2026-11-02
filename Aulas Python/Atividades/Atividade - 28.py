import random

list1 = []
list2 = []
list3 = []
list4 = []

for i in range (16):
    numero = random.randrange(1,100)
    if i <= 3:
        list1.append(numero)
    if i > 3 and i <= 7:
        list2.append(numero)
    if i > 7 and i <= 11:
        list3.append(numero)
    if i > 11:
        list4.append(numero)

print(list1)
print(list2)
print(list3)
print(list4)