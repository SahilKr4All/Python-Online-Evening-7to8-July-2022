Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list - list is a python's ordered and mutable data collection
x = [1,2,3,4,5,True,"Hello",34.345,5+3j]
type(x)
<class 'list'>
#indexing
x[0]
1
x[-1]
(5+3j)
x[-2]
34.345
x = [1,2,3,4,5,[6,7,8,[9,10,11,12]]]
#nested list
x[5]
[6, 7, 8, [9, 10, 11, 12]]
x[5][3][1]
10
x = [1,2,3,4,5,6,7,8]
x[0:6]
[1, 2, 3, 4, 5, 6]
x[::-1]
[8, 7, 6, 5, 4, 3, 2, 1]
#reverse of list
x = []
x.append(10)
x
[10]
x.append(100)
x
[10, 100]
x.append(1000)
x.append(-10000)
x
[10, 100, 1000, -10000]
x.insert(0,"ESS")
x
['ESS', 10, 100, 1000, -10000]
x.insert(1,"Institute")
x
['ESS', 'Institute', 10, 100, 1000, -10000]
#deletion
x
['ESS', 'Institute', 10, 100, 1000, -10000]
x.pop()
-10000
x
['ESS', 'Institute', 10, 100, 1000]
#pop()-it removes value of last index
x.pop(1)#pop(2)-it will remove the value of 2nd Index
'Institute'
x
['ESS', 10, 100, 1000]
#remove elements by value
x
['ESS', 10, 100, 1000]
x.remove(10)
x
['ESS', 100, 1000]
x = [10,10,10,20,300,50]
x.remove(10)
x
[10, 10, 20, 300, 50]
del x[-1]
x
[10, 10, 20, 300]
x.clear()
x
[]
del x#it will remove x from the memory
x
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x
NameError: name 'x' is not defined
x = [1,2,3,4]
#update
x[-1]=1000
x
[1, 2, 3, 1000]

x = [1,2,3,4]
y = [5,6,7,8]
x+y
[1, 2, 3, 4, 5, 6, 7, 8]
x.extend(y)
x
[1, 2, 3, 4, 5, 6, 7, 8]
x*y
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'list'
x-y
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    x-y
TypeError: unsupported operand type(s) for -: 'list' and 'list'
x/y
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x/y
TypeError: unsupported operand type(s) for /: 'list' and 'list'
x = [1,2,3,4]
x*2
[1, 2, 3, 4, 1, 2, 3, 4]
x**100
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    x**100
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
x*100
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
x = [i for i in range(1,101)]
#list comprehension
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
len(x)
100
x = [1,2,-100,-50,1000,0]
x.sort()
x
[-100, -50, 0, 1, 2, 1000]
x.sort(reverse=True)
x
[1000, 2, 1, 0, -50, -100]
#deep copy vs shallow copy
x = [1,2,3,4,5,6]
y = x
x
[1, 2, 3, 4, 5, 6]
y
[1, 2, 3, 4, 5, 6]
x.pop()
6
x
[1, 2, 3, 4, 5]
y
[1, 2, 3, 4, 5]
id(x)
2526878668160
id(y)
2526878668160

x = [1,2,3,4]
y = x.copy()
x
[1, 2, 3, 4]
y
[1, 2, 3, 4]
id(x)
2526841854784
id(y)
2526878668928
x.pop()
4
x
[1, 2, 3]
y
[1, 2, 3, 4]

x = [1,2,3,4,[5,6,7]]
y = x.copy()
x
[1, 2, 3, 4, [5, 6, 7]]
y
[1, 2, 3, 4, [5, 6, 7]]
del x[4][1]
x
[1, 2, 3, 4, [5, 7]]
y
[1, 2, 3, 4, [5, 7]]
id(x[4])
2526878669952
id(y[4])
2526878669952
#shallow copy
#deep copy
from copy import deepcopy
x
[1, 2, 3, 4, [5, 7]]
y = deepcopy(x)
del x[4][0]
x
[1, 2, 3, 4, [7]]
y
[1, 2, 3, 4, [5, 7]]
id(x[4])
2526878669952
id(y[4])
2526878608256
