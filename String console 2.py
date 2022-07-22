Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string functions
x = "Hello Python"
x.center("*")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x.center("*")
TypeError: 'str' object cannot be interpreted as an integer
x.center(2,'*')
'Hello Python'
len(x)
12
x.center(13,"*")
'*Hello Python'
x.center(14,"*")
'*Hello Python*'
x.center(24,"*")
'******Hello Python******'
x.center(25)
'       Hello Python      '
x = x.center(24,"^")
x
'^^^^^^Hello Python^^^^^^'
x.lstrip("^")
'Hello Python^^^^^^'
x.rstrip("^")
'^^^^^^Hello Python'
x.strip()
'^^^^^^Hello Python^^^^^^'
x.strip("^")
'Hello Python'
x = "hello"
x.startswith("h")
True
x.endswith("x")
False
x
'hello'
x.islower()
True
x.isupper()
False
x
'hello'
x.isalpha()
True
x = "hello1213"
x.isalpha()
False
x.isalnum()
True
x = "Hello Everyone"
x.replace("Hello","Bye")
'Bye Everyone'
