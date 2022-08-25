Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 'c'
type(x)
<class 'str'>
x = " ESS Institute"
type(x)
<class 'str'>
x = "Hello "Ravi""
SyntaxError: invalid syntax
x = 'Hello "Ravi"'
print(x)
Hello "Ravi"
x = "Hello \"Ravi\""
print(x)
Hello "Ravi"
#Indexing
x
'Hello "Ravi"'
x[0]
'H'
x[-1]
'"'
x[-2]
'i'
#Slicing
x[0:4]
'Hell'
x[0:5]
'Hello'
x[0:]
'Hello "Ravi"'
x[5:]
' "Ravi"'
x[0:5:1]
'Hello'
x[0:5]
'Hello'
x[0:10:3]
'Hl"v'
x
'Hello "Ravi"'
x[::-1]
'"ivaR" olleH'
x = "Hello"
x[::-1]
'olleH'
#String reverse
x = "Hello everyOne Welcome to Python Class"
x.lower()
'hello everyone welcome to python class'
x.upper()
'HELLO EVERYONE WELCOME TO PYTHON CLASS'
x.capitalize()
'Hello everyone welcome to python class'
x
'Hello everyOne Welcome to Python Class'
x.swapcase()
'hELLO EVERYoNE wELCOME TO pYTHON cLASS'
x.title()
'Hello Everyone Welcome To Python Class'
x
'Hello everyOne Welcome to Python Class'
x.find("P")
26
x[26]
'P'
x.find("o")
4
x.rfind("o")
30
x.find("o",5)
19
x.index("o",5)
19
 x.find("X")
 
SyntaxError: unexpected indent
x.find("X")
-1
#-1 - value not found
x.index("X")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x.index("X")
ValueError: substring not found
x
'Hello everyOne Welcome to Python Class'
x.replace("Python","Java")
'Hello everyOne Welcome to Java Class'
x
'Hello everyOne Welcome to Python Class'
x.count('l')
4
x
'Hello everyOne Welcome to Python Class'
x.split()
['Hello', 'everyOne', 'Welcome', 'to', 'Python', 'Class']
x.split("l")
['He', '', 'o everyOne We', 'come to Python C', 'ass']
