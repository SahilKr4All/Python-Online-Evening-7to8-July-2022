Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple
# tuple is python's immutable data collection
x = (1,2,3,4,5,6)
x
(1, 2, 3, 4, 5, 6)
y = [1,2,3,4,5,6]
#mutable
y[0] = 1000
x
(1, 2, 3, 4, 5, 6)
y
[1000, 2, 3, 4, 5, 6]
x[0] = 1000
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x[0] = 1000
TypeError: 'tuple' object does not support item assignment
help(tuple)
Help on class tuple in module builtins:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

x = (1,2,3,4,5,6,6,6,6,6,6)
x.count(6)
6
x.index(4)
3
x = {"rollNo":101,"Name":"Lokesh","Class":10}
x.keys()
dict_keys(['rollNo', 'Name', 'Class'])
x.values()
dict_values([101, 'Lokesh', 10])
x.items()
dict_items([('rollNo', 101), ('Name', 'Lokesh'), ('Class', 10)])

#CRUD - Create Read Update Delete
x = {}
type(x)
<class 'dict'>
x = dict()
type(x)
<class 'dict'>
#dictionary - python's unordered(No Indexing) data collection
x
{}
x["id"] = 1
x
{'id': 1}
x ["name"]="Ravi"
x
{'id': 1, 'name': 'Ravi'}
x['Class'] = 12
x
{'id': 1, 'name': 'Ravi', 'Class': 12}
x["name"]="Lokesh"#update
x
{'id': 1, 'name': 'Lokesh', 'Class': 12}
#delete
x
{'id': 1, 'name': 'Lokesh', 'Class': 12}
x.popitem()
('Class', 12)
#it will remove last key:value pair
x.pop('id')
1
x
{'name': 'Lokesh'}
del x['name']
x
{}

 x ={"rollNo":101,"Name":"Lokesh","Class":10}
 
SyntaxError: unexpected indent
x= {"rollNo":101,"Name":"Lokesh","Class":10}
x
{'rollNo': 101, 'Name': 'Lokesh', 'Class': 10}
x.get('rollNo')#it will return the value for the following key
101
