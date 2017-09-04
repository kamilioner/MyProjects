# class Calculator:
#     def power(self, n, p):
#         if (n < 0) or (p < 0):
#             raise Exception('n and p should be non-negative')
#         else:
#             wynik = 1
#             if n == 0:
#                 wynik -= 1
#             if p != 0:
#                 for i in range(p):
#                     wynik = wynik * n
#             return wynik

# import sys
#
# class Solution:
#     # Write your code here
#     def __init__(self):
#         stack = ''
#         queue = ''
#     def pushCharacter(self, ch):
#         self.stack = self.stack + str(ch)
#     def enqueueCharacter(self, ch)://Write your code here
#
#         self.queue =  str(ch) + self.queue
#     def popCharacter(self):
#         a = self.stack[0]
#         self.stack = self.stack[1:len(self.stack)]
#         return a
#     def dequeueCharacter(self):
#         a = self.queue[0]
#         self.queue = self.queue[1:len(self.queue)]
#         return a
#
#
# s = input()
# # Create the Solution class object
# obj = Solution()
#
# l = len(s)
# # push/enqueue all the characters of string s to stack
# for i in range(l):
#     obj.pushCharacter(s[i])
#     obj.enqueueCharacter(s[i])
#
# isPalindrome = True
# '''
# pop the top character from stack
# dequeue the first character from queue
# compare both the characters
# '''
# for i in range(l // 2):
#     print(obj.stack, obj.queue)
#     if obj.popCharacter() != obj.dequeueCharacter():
#         isPalindrome = False
#         break
# # finally print whether string s is palindrome or not.
# if isPalindrome:
#     print("The word, " + s + ", is a palindrome.")
# else:
#     print("The word, " + s + ", is not a palindrome.")

# n = int(input().strip())
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
#
# def swap(s1, s2):
#     tmp = a[s1]
#     a[s1] = a[s2]
#     a[s2] = tmp
#
# swaps = 0
# for i in range(n):
#     numberOfSwaps = 0
#     for j in range(n-1):
#         if a[j] > a[j + 1]:
#             swap(j, j + 1)
#             numberOfSwaps += 1
#             swaps += 1
#         j += 1
#
#     if numberOfSwaps == 0:
#         break
#
# print('Array is sorted in {} swaps.'.format(swaps))
# print('First Element: {}'.format(a[0]))
# print('Last Element: {}'.format(a[len(a)-1]))

