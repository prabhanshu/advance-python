"""
New-style classes unify the concepts of class and type.
If obj is an instance of a new-style class, type(obj) is the same as obj.__class__:
"""


class Foo:
    pass


obj = Foo()
print("__class__")
print(obj.__class__)  # <class '__main__.Foo'>
print("type")
print(type(obj))  # <class '__main__.Foo'>


n = 5
d = {'x': 1, 'y': 2}

for x in (n, d, obj):
    print(type(x) is x.__class__)  # True, True, True
