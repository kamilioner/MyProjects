import random
import time

Tab = []
ilosc_sortowanych_liczb = 5000  # Musi być przysta
najwieksza_sortwana_liczna = 10000000


def losowe(L):
    L = []
    for i in range(0, ilosc_sortowanych_liczb):
        L.append(random.choice(range(0, najwieksza_sortwana_liczna)))
    return L


def czesciowo_losowe(L):
    L = []
    for i in range(0, (ilosc_sortowanych_liczb/2)):
        L.append(random.choice(range(0, najwieksza_sortwana_liczna)))
    L.sort()
    for i in range(((ilosc_sortowanych_liczb/2) + 1), ilosc_sortowanych_liczb):
        L.append(random.choice(range(0, najwieksza_sortwana_liczna)))
    return L


def rosnaco(L):
    L = []
    for i in range(0, ilosc_sortowanych_liczb):
        L.append(random.choice(range(0, najwieksza_sortwana_liczna)))
    L.sort()
    return L


def malejaco(L):
    L = []
    for i in range(0, ilosc_sortowanych_liczb):
        L.append(random.choice(range(0, najwieksza_sortwana_liczna)))
    L.sort(reverse=True)
    return L


def Sortowanie_wstawianie(A):
    startm = int(round(time.time() * 1000))
    for i in range(1, len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = klucz
    stopm = int(round(time.time() * 1000))
    # print(A)
    return (stopm - startm)


def Sortowanie_wybor(A):
    startm = int(round(time.time() * 1000))
    for i in range(0, len(A)):
        klucz = A[i]
        k = i
        j = i + 1
        for j in range((i + 1), len(A)):
            if klucz > A[j]:
                klucz = A[j]
                k = j
        A[k] = A[i]
        A[i] = klucz
    stopm = int(round(time.time() * 1000))
    # print(A)
    return (stopm - startm)


def Sortowanie_zliczanie(A):
    startm = int(round(time.time() * 1000))
    t = max(A) + 1
    tmp = [0] * (t)
    for i in A:
        tmp[i] += 1
    j = 0
    for a in range(t):
        for c in range(tmp[a]):
            A[j] = a
            j += 1
    stopm = int(round(time.time() * 1000))
    # print(A)
    return (stopm - startm)


Tab = losowe(Tab)
# Tab = czesciowo_losowe(Tab)
# Tab = rosnaco(Tab)
# Tab = malejaco(Tab)
# print (Tab)
print("Czas sortowania przez wstawianie: ", Sortowanie_wstawianie(Tab))
print("Czas sortowania przez wybor:", Sortowanie_wybor(Tab))
print("Czas sortowania przez zliczanie", Sortowanie_zliczanie(Tab))


