Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#set - set is a python's unordered(no-indexing/slicing) data collection
x = set()
x
set()
x.add(1)
x.add(2)
x.add(3)
x
{1, 2, 3}
type(x)
<class 'set'>
x.remove(2)
x
{1, 3}
#set - set cannot contain duplicate values
x = {1,2,2,2,2,1,1,1,4,4,4,5}
x
{1, 2, 4, 5}
x = {1,2,3,4}
y = {3,4,5,6}
#union- All but without repetition
x.union(y)
{1, 2, 3, 4, 5, 6}
x.intersection(y)# - common elements
{3, 4}
x.intersection(y)
{3, 4}
x
{1, 2, 3, 4}
y
{3, 4, 5, 6}
x-y
{1, 2}
y-x
{5, 6}
x.difference(y)
{1, 2}
x
{1, 2, 3, 4}
y.differece(x)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    y.differece(x)
AttributeError: 'set' object has no attribute 'differece'. Did you mean: 'difference'?
y.difference(x)
{5, 6}
