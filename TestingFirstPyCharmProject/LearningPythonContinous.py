# def recur2(i):
#     print(i)
#     if i > 0:
#         recur2(i-1)
#
# recur2(10)
#

# ###Ex1:
#
# def funct(A):
#     higherNumber = max(A)
#     return A.index(higherNumber)
#
# print(funct([2, 4, 6, 3, 10, 2, 0]))

# ###Ex2:
#
# def cutter(word):
#     shortened = 0
#     if len(word) < 4:
#         printer = word
#     else:
#         if (word[:3] in ("pre", "pro", "con", "com")):
#             temp_word = word[3:]
#             shortened = 1
#         else:
#             if (word[:4] in ("post", "para")):
#                 temp_word = word[4:]
#                 shortened = 1
#             else:
#                 temp_word = word
#         if (temp_word[(len(temp_word)-2):]) in ("ed"):
#             printer = temp_word[:len(temp_word)-2]
#             shortened = 1
#         else:
#             if (temp_word[(len(temp_word) - 3):]) in ("ing", "ate"):
#                 printer = temp_word[:len(temp_word) - 3]
#                 shortened = 1
#             else:
#                 if (temp_word[(len(temp_word) - 4):]) in ("tion", "ment"):
#                     printer = temp_word[:len(temp_word) - 4]
#                     shortened = 1
#                 else:
#                     printer = temp_word
#
#     if shortened != 1:
#         print("Word cannot be shortened")
#     else:
#         print("Word has been shortened")
#     return printer
#
# print(cutter("king"))
# ### Ex.3
# import math
#
#
# def combination(n, r):
#     return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))
#
#
# def pascals_triangle(rows):
#     result = []
#     for count in range(rows):
#         row = []
#         for element in range(count + 1):
#             row.append(combination(count, element))
#         result.append(row)
#     return result
#
#
# def ready_triange(number):
#     for row in pascals_triangle(number):
#         print(row)
#
#
# ready_triange(10)
#
# ### Ex. 4 (File read)
#
# number_of_lines = 0
# f = open("text.txt", "r")
# for line in f:
#     number_of_lines += 1
#     if ("you " in line) or (" you" in line):
#         print(str(number_of_lines) + ": " + line)
#

### Ex. 5 (CSV testing)


import re
import csv

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

table_name = 'test_table2'
line = 1
data_list = []
file_delimiter = ','
data_quotechar = '*'
create_table_string = 'CREATE TABLE '
create_table_string += table_name
create_table_string += ' ('

my_csv_file = open("procesy.csv", "r")
my_csv_reader = csv.reader(my_csv_file, delimiter=file_delimiter, quotechar=data_quotechar)
my_csv_data = list(my_csv_reader)


for word in range(len(my_csv_data[line])):

    my_csv_data[line][word] = re.sub('"', '', my_csv_data[line][word])

    if my_csv_data[line][word] == '':
        data_list.append('VARCHAR(200)')
    else:
        if isint(my_csv_data[line][word].rstrip()):
            data_list.append('INT')
        else:
            if isfloat(my_csv_data[line][word].rstrip()):
                data_list.append('FLOAT')
            else:
                data_list.append('VARCHAR(200)')

if line == 1:
    for cl in range(len(data_list)):
        create_table_string += ((my_csv_data[0][cl]).rstrip() + ' ' + (data_list[cl]).rstrip() + ', ')
if line == 0:
    for cl in range(len(data_list)):
        create_table_string += ('expr' + str(cl+1) + ' ' + (data_list[cl]).rstrip() + ', ')

create_table_string = create_table_string[:-1]
create_table_string = create_table_string[:-1]
create_table_string += ')'
print(create_table_string)
print('')
print('')

for csv_file_lines in range(len(my_csv_data)):
    if csv_file_lines == 1:
        insert_row_string = 'INSERT INTO '
        insert_row_string += table_name
        insert_row_string += ' ('
        for cl in range(len(data_list)):
            insert_row_string += ((my_csv_data[0][cl]).rstrip() + ', ')
        insert_row_string = insert_row_string[:-1]
        insert_row_string = insert_row_string[:-1]
        insert_row_string += ') VALUES ('
        for word in range(len(my_csv_data[csv_file_lines])):
            my_csv_data[csv_file_lines][word] = re.sub('"', '', my_csv_data[csv_file_lines][word])
            if isfloat(my_csv_data[csv_file_lines][word].rstrip()):
                insert_row_string += (my_csv_data[csv_file_lines][word].rstrip() + ", ")
            else:
                insert_row_string += ("'" + my_csv_data[csv_file_lines][word].rstrip() + "'" + ", ")
        insert_row_string = insert_row_string[:-1]
        insert_row_string = insert_row_string[:-1]
        insert_row_string += ')'
        print(insert_row_string)

my_csv_file.close()
#
# import xlsxwriter
#
#
# Create an new Excel file and add a worksheet.
# workbook = xlsxwriter.Workbook('demo.xlsx')
# worksheet = workbook.add_worksheet()
#
# Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 20)
#
# Add a bold format to use to highlight cells.
# bold = workbook.add_format({'bold': True})
#
# Write some simple text.
# worksheet.write('A1', 'Hello')
#
# Text with formatting.
# worksheet.write('A2', 'World', bold)
#
# Write some numbers, with row/column notation.
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)
#
# Insert an image.
# worksheet.insert_image('B5', 'logo.png')
#
# workbook.close()
#


# import sys

# a, b = input().strip().split(' ')
# a, b = [int(a), int(b)]
# table = input().strip().split(' ')
#
# if a < b:
#     for i in range(b):
#         tabletmp = table[1:a + 1]
#         tabletmp.append(table[0])
#         table = tabletmp
# else:
#     tabletmp = (table[b:a] + table[0:b])
#     table = tabletmp
#
# print(' '.join(table))

# ###
#
# a = input()
# aa = []
# for i in range(int(a)):
#     aa.append(str(input()))
# b = input()
# bb = []
# for i in range(int(b)):
#     bb.append(str(input()))
#
# for i in range(len(bb)):
#     counter = 0
#     for j in range(len(aa)):
#         if bb[i] == aa[j]:
#             counter += 1
#     print(counter)
#
# ###


# n, m = map(int, input().split())
# tab_a = []
# #tab_b = []
# for i in range(n+1):
#     tab_a.append(0)
# for i in range(m):
#     a, b, k = map(int, input().split())
#     tab_a[a-1] += k
#     tab_a[b] -= k
#
# print(tab_a)
#
# sumt = 0
# maxt = 0
#
# for i in range(n):
#     sumt += int(tab_a[i])
#     maxt = max(maxt, sumt)
#
#
# print(maxt)


# for i in range(b):
#     for j in range(tab_b[i][0]-1, tab_b[i][1]):
#         tab_a[j] += tab_b[i][2]

# print(max(tab_a))
#
# a, b = map(int, input().split())
# tab_a = []
# for i in range(a):
#     tab_a.append(0)
# for i in range(b):
#     m, n, k = map(int, input().split())
#     for j in range(m-1, n):
#         tab_a[j] += k
#
# # print(tab_a)
# # print(tab_b)
# #
# # for i in range(b):
# #     for j in range(tab_b[i][0]-1, tab_b[i][1]):
# #         tab_a[j] += tab_b[i][2]
#
# print(max(tab_a))
#
# class Person:
#     age = 0
#     def __init__(self,initialAge):
#         # Add some more code to run some checks on initialAge
#         if initialAge <= 0:
#             Person.age = 0
#             print("Age is not valid, setting age to 0.")
#         else:
#             Person.age = initialAge
#     def amIOld(self):
#         if Person.age < 13:
#             print("You are young.")
#         if Person.age >= 13 and Person.age < 18:
#             print("You are a teenager.")
#         if Person.age >= 18:
#             print("You are old.")
#         # Do some computations in here and print out the correct statement to the console
#     def yearPasses(self):
#         Person.age += 1
#         # Increment the age of the person in here
#
# t = int(input())
# for i in range(0, t):
#     age = int(input())
#     p = Person(age)
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()
#     p.amIOld()
#     print("")

# n = input()
# for i in range(int(n)):
#     word = input()
#     new_word = []
#     iteration = 0
#     for j in range(len(word)):
#         try:
#             new_word.extend(word[iteration])
#         except:
#             pass
#         iteration += 2
#     new_word.extend("  ")
#     iteration = 1
#     for k in range(len(word)):
#         try:
#             new_word.extend(word[iteration])
#         except:
#             pass
#         iteration += 2
#     print(''.join(new_word))
#
#
# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# n_arr = []
# for i in range(len(arr)):
#     n_arr.extend(str(arr[len(arr) - i -1]))
# print(" ".join(n_arr))
#
# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# arr.reverse()
# print(*arr)
#
# n = input()
# phonebook = {}
# for i in range(int(n)):
#     a, b = input().strip().split(' ')
#     phonebook[a] = {b}
#
# for i in range(int(n)):
#     c = input()
#     if c in phonebook:
#         print(c + "=" + str(*phonebook[c]))
#     if c not in phonebook:
#         print("Not found")

# a = int(input())
#
# def toBinary(n):
#     return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])
#
# number = 0
# print(toBinary(a))
# p = str(toBinary(a))
# for i in range(63):
#     if (p[i] == p[i+1]) and (int(p[i]) == 1):
#         number += 1
#
# print(number)
#
# a = int(input())
#
# def toBinary(n):
#     return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])
#
# #print(toBinary(a))
# p = str(toBinary(a))
# print(len(max(p.split("0"))))

# s = input().strip()
# t = input().strip()
# k = int(input().strip())
#
# shorter = 0
# the_same = 0
# if len(s) < len(t):
#     shorter = len(s)
# else:
#     shorter = len(t)
# i = 0
#
#
# for a in range(shorter):
#     if s[the_same] != t[the_same]:
#         break
#     if s[the_same] == t[the_same]:
#         the_same += 1
#
# rest_s = len(s)-the_same
# rest_t = len(t)-the_same
#
# if rest_s + rest_t <= k:
#     print("Yes")
# else:
#     print("No")

# import math
# n = int(input())
# for i in range(n):
#     a, b = map(int, input().split())
#     if math.sqrt(a).is_integer():
#         a = int(math.sqrt(a))
#     else:
#         a = int(math.sqrt(a))+1
#     b = int(math.sqrt(b))
#     print(b-a+1)
#
# def array_left_rotation(a, n, k):
#     tmp = []
#     for i in range(k):
#         tmp = a[1:n]
#         tmp.extend(str(a[0]))
#         a = tmp
#     return a
#
# n, k = map(int, input().strip().split(' '))
# a = list(map(int, input().strip().split(' ')))
# answer = array_left_rotation(a, n, k);
# print(*answer, sep=' ')

# a, b = input().strip().split(' ')
# a, b = [int(a), int(b)]
# table = input().strip().split(' ')
#
# if a < b:
#     for i in range(b%a):
#         tabletmp = table[1:a + 1]
#         tabletmp.append(table[0])
#         table = tabletmp
# else:
#     tabletmp = (table[b:a] + table[0:b])
#     table = tabletmp
#
#
#
# print(' '.join(table))
#
#
# text = "ABRACADABRA"
# for i in range(len(text)):
#     print(''.join(text[0:i + 1]))
