# import os
# print(os.path.expanduser('~'))
#
# import re
# print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com"))
#
#



list = ['a', 'b', 'c', 'd', 'e']
print (list[::-1])








# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')
#
# print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)
#
#

# # Multiple inheritance
# class Father():
#     def fatherclass(self):
#         print("Father Class")
#
# class Mother():
#     def motherclass(self):
#         print("Mother class")
#
# class Child(Father,Mother):
#     def childclass(self):
#         Father.fatherclass(self)
#         Mother.motherclass(self)
#         print("Child Class")
#
#
# c = Child()
# c.childclass()

#Exception Handling :

# class Floor(Exception):
#     def __init__(self,msg)
# :
#         self.msg = msg
#
#
#     def print_Exception(self):
#         print("User defined Exception : ", self.msg)
#
#
# try:
#     raise Floor("Climbing to 5th floor and fell down")
# except Floor as e:
#     e.print_Exception()



# #File handling with Try except blocks
# def Process_file():
#     try:
#         f = open("C:\\Users\\AC30796\\PycharmProjects\\Create3.txt", "r")
#         print(f.read())
#         x = 1/0
#     except FileNotFoundError as e:
#         print(e)
#     except Exception as a:
#         print(a)
#     finally:
#         print("Cleaned and closed the file ")
#         f.close()
#
# Process_file()
#


# import time
#
# def time_it(func):
#
#     def inner(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__ + "took " +str((end-start)/12*60) + "Min")
#         return result
#     return inner
#
# @time_it
# def square(num):
#     r = []
#     for i in num:
#         r.append(i*i)
#     return r
#
# @time_it
# def cube(num):
#     r = []
#     for i in num:
#         r.append(i*i*i)
#     return r
#
#
# num = range(1,10000)
# lst1 = square(num)
# lst2 = cube(num)
#
# print(lst1)
# print(lst2)
#








# def smart(func):
#
#     def inner(a,b):
#         if a < b:
#             a, b =b, a
#         return func(a,b)
#     return inner
#
#
# @smart
# def div(a,b):
#     print(a/b)
#
#
#
# div(2,4)


# from functools import reduce
# lst = [2, 5, 3, 8, 9, 11, 10, 12]
#
# evens = list(filter(lambda n: n % 2 == 0, lst))
# print(evens)
# doubles = list(map(lambda n : n * 2, evens))
# print(doubles)
#
# last = reduce(lambda a, b: a+b, doubles)
# print(last)
#



#
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
#
# p = fact(4)
# print(p)

# def fact(n):
#     t = 1
#     for i in range(1,n+1):
#         t = t * i
#     print(t)
#
# fact(5)

#
# def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(b)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a+b
#             a = b
#             b = c
#             if c >= 100:
#                 break
#             print(c)
# fib(120)

# ##Finding even or odd from the list
# even = 0
# odd = 0
#
# def count(lst):
#     for i in lst:
#         if i%2 == 0:
#             globals()['even'] += 1
#         else:
#             globals()['odd'] += 1
#     return even,odd
#
#
#
# lst = [21,3,41,12,5,42]
#
# even , odd  = count(lst)
#
# print("Even : {} and odd : {}".format(even,odd))
#



# ##Number of chars in a name >5
# def userNameLength(c):
#     count = 0
#     for j in lst:
#         if len(j) > 5:
#             count += 1
#     return count
#
#
# lst = []
# lengthOfList = int(input("Enter the length of list : "))
#
# for i in range(0,lengthOfList):
#     app = input("Enter the list next value : ")
#     lst.append(app)
# print(lst)
#
# countVar = userNameLength(lst)
# print("Number of names greater than 5 chars : {}".format(countVar))
#

#
# def person(name, **data):
#     print(name)
#
#     for i,j in data.items():
#         print(i,j)
#
# person('Javed', age = 28, City = 'Bangalore', Field = 'B.Tech')
#
#

# def sum(*args):
#     c = 0
#     for i in args:
#         c = c + i
#
#     print(c)
#
# sum(1,5,2,3,4,5)
#
#
#

#
#
# def add(a,b):
#     x = a + b
#     y = a - b
#     return x,y
#
# s,sub = add(5,6)
# print(s, sub)
#

# from numpy import *
#
# m1 = matrix('1,2;3,4;5,6;7,8')
# m2 = matrix('6,7,8,9;1,2,4,6')
#
#
# m = m1 * m2
# print(m)
#



# a = array('i',[2,3,5,12,6])
# Max = a[0]
# for i in range(0, len(a)):
#     if a[i] >= Max:
#         Max = a[i]
#
# print(Max)


# a = array('i',[2,3,5,12,6])
# b = array('i',[4,6,2,9,1,8])
# c = array(a.typecode,[])
# j = len(a)
# k = len(b)
# l=0
# if j == k:
#     for i in a:
#         f = a[l]+b[l]
#         c.append(f)
#         l += 1
# else:
#     print("Array length is not matching")
# print(c)


















# arr = array([2,6,3,4,5])
#
# # num = (n*3 for n in arr)
# arr1 = arr.copy()
# arr1[1] = 7
# print(arr, arr1)
# print(id(arr1))
# print(id(arr))
#


# for i in range(10):
#     if not i%2 == 0:
#         print(i+1)




## Delete a element from array
# from array import *
# arr = array('i',[])
# n = int(input("Length of array: "))
# for i in range(n):
#     x = int(input("Enter the next value: "))
#     arr.append(x)
#
#
# newArr = array(arr.typecode, [])
# z = int(input("Enter the index number you wanted to delete from array : "))
# k = 0
# for i in arr:
#     if k != z:
#         newArr.append(i)
#     k += 1
# print(newArr)










# from array import *
#
# arr = array('i', [])
#
# n = int(input("Length of array: "))
#
# for i in range(n):
#     x = int(input("Enter the next value: "))
#     arr.append(x)
#
# print(arr)
#
# j = int(input("Enter the search: "))
# k = 0
# for e in arr:
#     if e == j:
#         print(k)
#         break
#     k += 1
# print(arr.index(j))







##Factorial of a number
#
# n = int(input("Enter a no: "))
# t = 1
# for i in range(1, n+1):
#     t = t * i
# print(str(t))
#


#
# from array import *
# arr = array('i',[3, 6, 5, 4, 7, 2, 9])
# print(arr)
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)
#


##Prime number in efficient way

#
# num = 1
# if num <= 1:
#     print("not defined")
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
#
#









##
#
# l1 = ['A', 'B', 'C', 'D']
# l2 = ['p', 'Q', 'R']
#
# for i in range(4):
#     print(l1[:i+1], l2[i:])
#
#
#

#
# i = 1
# j = 1
#
# for i in range(1,5):
#     for j in range(i,5):
#         print(j, end="")
#         j += 1
#     i += 1
#     print()
#















## Prime number
# x = int(input("Enter a no: "))
# a = 0
# i = 1
# while i <= x:
#     if x % i == 0:
#         a += 1
#     i += 1
# if a == 2:
#     print("It is a prime number")
# else:
#     print("Not a prime number")


##Fibonacci series

# n = int(input("Enter a number for Fibonacci : "))
# i = 0
# j = 1
# count = 0
# if n == 1:
#     print("1")
# else:
#     while count < n:
#         print(i)
#         x = i + j
#         i = j
#         j = x
#         count += 1
#
#











##Vending machine
# candies = 5
# i = 0
# x = int(input("Number of candies required? : "))
# while i <= x:
#     if i >= candies:
#         print("There are only " + str(candies) + " candies available")
#         break
#     print("Candy")
#     i += 1




## Perfect Square roots
# import math as m
# for i in range(1,500):
#     if i % m.sqrt(i) == 0:
#         print(int(m.sqrt(i)), "is perfect square root of ",i)


# printing #
# i = 1
# while i <= 4:
#     print(5*'#')
#     i += 1

#
# i = 1
# j = 1
# for i in range(4):
#     for j in range(4):
#         print("#", end="")
#         j += 1
#     i += 1
#     print()


#
# i = 1
# j = 1
# for i in range(4):
#     for j in range(4-i):
#         print("#", end="")
#         j += 1
#     i += 1
#     print()


## Divisible by 3 and 5
# While loop# lst = list(range(100))
# j = 0
# while lst[j] <= 101:
#     if lst[j] % 3 != 0 and lst[j] % 5 != 0:
#         print("Skipped number", lst[j])
#     else:
#         print(lst[j])
#     j = j+1

# i= 1
#
# while i <= 5:
#     print('Telusko', end=" ")
#     j = 1
#     while j<=4:
#         print("Javed", end="")
#         j = j+1
#     i = i+1
#     print()



##Largest among 3 values
# x, y, z = int(input("X :  ")), int(input("Y : ")),int(input("Z : "))
#
# if x >= y and x >= z:
#     print('x is large')
# elif y >= x and y >= z:
#     print('y is large')
# else:
#     print('z is large')




# -ve or +ve number
# if x >= 0:
#     print("+ve number")
# else:
#     print("-ve Number")
#

##Even or Odd number
# x = int(input("Enter a value "))
#
# y = x % 2
#
# if y == 0:
#     print("Even")
# else:
#     print("Odd")


