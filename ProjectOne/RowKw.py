import cmath

a = float
b = float
c = float
z = False

while not z:
    try:
        a = float(input('Podaj a: '))
        b = float(input('Podaj b: '))
        c = float(input('Podaj c: '))
        z = True
    except:
        print("Podaj inne wartości!")

if (a == 0):
    if (b == 0):
        if (c == 0):
            print("Równianie tożsamościowe")
        else:
            print("Równanie sprzeczne")
    else:
        print("Równanie liniowe o rozwiazaniu x=", c / b)

else:
    d = (b * b) - (4 * a * c)

    if d == 0:
        x12 = (-b / (2 * a))
        print('x1/2 = {0} '.format(x12))

    if d != 0:
        x1 = (-b - cmath.sqrt(d)) / (2 * a)
        x2 = (-b + cmath.sqrt(d)) / (2 * a)
        print('x1 = {0}, x2 = {1}'.format(x1, x2))
