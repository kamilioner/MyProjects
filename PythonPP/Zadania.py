a = 2.1     #float
b = "abc"   #string
c = 0         #int

print(str(a)+" " + b + " " + str(c))

###

c += 31.3

chleb = 1.99
mleko = 2.50
Cukierek = 12.99

print(2*chleb + 0.5 * mleko + 0.3 * Cukierek)

(2+5j) + (4+6j)
4 -(4+6j)

imie = "kamil"
nazw = "budka"
wiek = 24
pensja = 3245.23
stanowisko = "programista"

print(imie + " " + nazw + " " + str(wiek) + " " + str(pensja) + " " + stanowisko)

for i in range(10):
    print("powyzszy napis")

kwadrat = 2
print(kwadrat * kwadrat)
a_tr = 3
b_tr = 6
c_tr = 4
print(a_tr + b_tr + c_tr)
kolo = 3
print(kolo*kolo*3.14)

a = 0
b = 1
if ~(a and b) == (~a or ~b):
    print("true")

a = "awn"
b = 3
c = 5.8

# a < b
# b > c
# a == b
# c != a
# b <> c
# a <= b
# c >= c

a = 17**(1/2)
print(str(a)+"j")


print((str(55) + ",")*20)

print("Podaj imie:")
a = input()
print("Witaj "+ a)

def powiel(a):
    for i in range(30):
        print(a)

powiel("hej")

print("podaj N")
n = input()
print("podaj SPK")
sp = input()
print("podaj P")
p = input()

print(str((float(sp) + float(sp) * float(p)/100) ** int(n)))
lista = ["p1","p2","p3","p4"]
lista_kursow = ["C#", "C++", "Java", "Python"]

lista.extend(lista_kursow)
print(lista)

lista = lista[:4]
print(lista)

data = ("21", "03", "2019")
print(data[0]+"."+data[1]+"."+data[2])

import random

pustalista = [0,0,0,0,0,0]
i = 0

while pustalista[5] == 0:
    a = random.randint(1,49)
    if a not in pustalista:
        pustalista[i] = a
        i += 1

print(pustalista)

listapunktow = []

for i in range(11):
    listapunktow.append("("+str(i)+","+str(i*2)+")")

print(listapunktow)
