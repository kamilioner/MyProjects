# ### Print
#
# a = ['Mary', 'had', 'a', 'little', 'lamb']
#
# for i in range(len(a)):
#     print(i, a[i])
#

# ### Breaking
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n // x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
#
# ### The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. For example:
#
# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
#
# class MyEmptyClass:
#     pass
#
# def initlog(*args):
#     pass   # Remember to implement this!
#
# ### Defining Functions
#
# def fib(n):  # write Fibonacci series up to n
#     #Print a Fibonacci series up to n.
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()
#
# fib(2000)
#
# ### scopes
#
# i = 5
#
# def f(arg=i):
#     print(arg)
#
# i = 6
# f() ###prints 5
#
# ###Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:
#
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
# ###accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be called in any of the following ways:
#
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
#
# ### but all the following calls would be invalid:
# #
# # parrot()                     # required argument missing
# # parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# # parrot(110, voltage=220)     # duplicate value for the same argument
# # parrot(actor='John Cleese')  # unknown keyword argument
#
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print(kw, ":", keywords[kw])
#
# ###It could be called like this:
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")
#
# ###and of course it would print:
#
# # -- Do you have any Limburger ?
# # -- I'm sorry, we're all out of Limburger
# # It's very runny, sir.
# # It's really very, VERY runny, sir.
# # ----------------------------------------
# # client : John Cleese
# # shopkeeper : Michael Palin
# # sketch : Cheese Shop Sketch
#
# ### Use CamelCase for classes and lower_case_with_underscores for functions and methods.
#
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits)
# print("")
# print("fruits.count('apple')")
# print(fruits.count('apple'))
# print("fruits.count('tangerine')")
# print(fruits.count('tangerine'))
# print("fruits.index('banana')")
# print(fruits.index('banana'))
# print("fruits.index('banana', 4)  # Find next banana starting a position 4")
# print(fruits.index('banana', 4))  # Find next banana starting a position 4
# print("fruits.reverse()")
# fruits.reverse()
# print(fruits)
# print("fruits.append('grape')")
# fruits.append('grape')
# print(fruits)
# print("fruits.sort()")
# fruits.sort()
# print(fruits)
# print("fruits.pop()")
# print(fruits.pop())
#
# ### To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:
#
#
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# print(queue.popleft())                 # The first to arrive now leaves
# print(queue.popleft())                 # The second to arrive now leaves
# print(queue)                           # Remaining queue in order of arrival

####

#
# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])

####

#
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(matrix)
# matrix.append([13, 14, 15, 16])
# print(matrix)
#
# def transform_matrix(a_matrix):
#     matrix_tmp = []
#     for i in range(len(a_matrix)):
#         matrix_tmp.append([row[i] for row in a_matrix])
#     return matrix_tmp
#
# print(list(zip(*matrix)))
# matrix = transform_matrix(matrix)
# print(matrix)
#
# s = input("Input an integer: ")
# try:
#     k = int(s)
#     ks = k/2
# except:
#     z = float(s)
#     ks = int(z/2)
# print(ks)
#
####
# import sys
#
# for arg in sys.argv[1:]:
#     # count = 0
#     table = []
#     file = str('"' + arg + '"')
#     print(file)
#     try:
#         f = open(arg, "r")
#         for line in f:
#             table_line = []
#             for word in line.split(','):
#                 table_line.append(word)
#             if table_line[2] == "ESCAMBIA COUNTY":
#                 table.append(line)
#         f.close()
#         for w in table:
#             print(str(w).rstrip())
#     except:
#         print("Error on file: " + file)
#
# import random
#
# for i in range(0, 2):
#     f = open("testfile" + str(i) + ".txt", "w")
#     for number in range(0, 100):
#         f.write(str(random.randrange(1000)))
#         f.write("\n")
#     f.close()


####

# list_of_signs = []
# for i in range(0, 2):
#     f = open("testfile"+str(i)+".txt", "r")
#     for number in f:
#         list_of_numbers.append(int(number))
#     f.close()
# n = open("sorted.txt", "w")
# list_of_numbers.sort()
# for a in list_of_numbers:
#     n.write(str(a))
#     n.write("\n")
# n.close()
# s_table = []
# s = "937987095073jnkjanhjwnuidnajkcipumxioejijalwkmwioj76087903875"
# for a in s:
#     s_table.append(a)
# s_table.sort()
# print(s_table)

####

# class person:
#     def __init__(self, name):
#         self.name = name
#         self.introductions = False
#
#     def introduce(self):
#         print ("Hi, my name is ", self.name)
#         self.introductions = True
#
# me = person("Jim")
# print(me.introductions)
# me.introduce()
# print(me.introductions)
###
# from math import sqrt
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def getx(self):
#         return self.__x
#
#     def gety(self):
#         return self.__y
#
#     def setx(self, x):
#         self.__x = x
#
#     def sety(self, y):
#         self.__y = y
#
#     def distance(self, p):
#         d = (self.__x - p.getx()) * (self.__x - p.getx()) + (self.__y - p.gety()) * (self.__y - p.gety())
#         return sqrt(d)
#
#     def move(self, dx, dy):
#         self.__x = self.__x + dx
#         self.__y = self.__y + dy
#
#     def draw(self):
#         print("(", self.__x, ",", self.__y, ") ")
#
#
# point_a = Point(-41, 96)
# point_b = Point(-39, 65)
# print(point_a.distance(point_b))
# point_a.draw()
#
# class Square:
#     def __init__(self, side=0):
#         self.__side = side
#
#     def area(self):
#         return self.__side * self.__side
#
#     def setside(self, x):
#         self.__side = x
#
#     def getside(self):
#         return self.__side
#
# newSquare = Square()
# newSquare.setside(12)
# print(newSquare.area())

# a = ''
# b = []
#
# b.append('aba')
# b.append('cbc')
# b.append('efg')
#
# for i in range(len(b)):
#     a += b[i]
#
# print(a)

# import re
#
# def isfloat(x):
#     try:
#         a = float(x)
#     except ValueError:
#         return False
#     else:
#         return True
#
# def isint(x):
#     try:
#         a = float(x)
#         b = int(a)
#     except ValueError:
#         return False
#     else:
#         return a == b
#
# a = ''
#
# a = re.sub('"', '', a)
# print("a = {}".format(a))
#
# # print(type(a))
# # try:
# #     a = float(a)
# #     print("{} is a float".format(a))
# #     try:
# #         a = int(a)
# #         print("{} is an int".format(a))
# #     except:
# #         print("{} is a string".format(a))
# # except:
# #     print("{} is a string".format(a))
# # print(type(a))
#
# if isint(a):
#     print("a is an int")
# else:
#     if isfloat(a):
#         print("a is a float")
#     else:
#         print("a is a string")
#
# a = '342,53256'
# a.rstrip()
# a = float(a)
# print(a)

# import csv
#
# table_name = 'test_table2'
# data_list = []
# file_delimiter = '|'
# new_file_delimiter = ','
# data_quotechar = '*'
# new_data_quotechar = "\""
# create_table_string = 'CREATE TABLE '
# create_table_string += table_name
# create_table_string += ' ('
#
# my_csv_file = open("new_test.csv", "r")
# my_new_csv_file = open("procesy.csv", "w")
# my_csv_reader = csv.reader(my_csv_file, delimiter=file_delimiter, quotechar=data_quotechar)
# my_csv_data = list(my_csv_reader)
#
# for line in range(len(my_csv_data)):
#     for word in range(len(my_csv_data[line])):
#         my_new_csv_file.write(new_data_quotechar + my_csv_data[line][word] + new_data_quotechar + new_file_delimiter)
#     my_new_csv_file.write('\n')
#
# my_new_csv_file.close()
# my_csv_file.close()

#
# n = 2
# for i in range(100):
#     a = 1 / (1 + (1 / n))
#     print(a)
#     n += 1

