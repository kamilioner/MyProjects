### sorting numbers in an extra file

list_of_numbers = []
list_of_signs = []
for i in range(0, 2):
    f = open("testfile"+str(i)+".txt", "r")
    for number in f:
        list_of_numbers.append(int(number))
    f.close()
n = open("sorted.txt", "w")
list_of_numbers.sort()
for a in list_of_numbers:
    n.write(str(a))
    n.write("\n")
n.close()
