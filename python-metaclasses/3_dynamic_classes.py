"""
The built-in type() function, when passed one argument, returns the type of an object.
For new-style classes, that is generally the same as the object’s __class__ attribute:
"""

print(type(3))  # <class 'int'>
print(type(['foo', 'bar', 'baz']))  # <class 'list'>
t = (1, 2, 3, 4, 5)
print(type(t))  # <class 'tuple'>


class Foo:
    pass


print(type(Foo))  # <class 'type'>
print(type(Foo()))  # <class '__main__.Foo'>


"""
You can also call type() with three arguments—type(<name>, <bases>, <dct>):

1) <name> specifies the class name. This becomes the __name__ attribute of the class.
2) <bases> specifies a tuple of the base classes from which the class inherits. 
    This becomes the __bases__ attribute of the class.
3) <dct> specifies a namespace dictionary containing definitions for the class body. 
    This becomes the __dict__ attribute of the class.

Calling type() in this manner creates a new instance of the type metaclass. 
In other words, it dynamically creates a new class.
"""
