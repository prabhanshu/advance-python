"""
Type and Class:
In Python 3, all classes are new-style classes.
Thus, in Python 3 it is reasonable to refer to an object’s type and its class interchangeably.

NOTE:
In Python 2, classes are old-style by default. Prior to Python 2.2, new-style classes weren’t supported at all.
From Python 2.2 onward, they can be created but must be explicitly declared as new-style.

REMEMBER:
in Python, everything is an object. Classes are objects as well.
As a result, a class must have a type. What is the type of a class?
"""


class Foo:
    pass


x = Foo()
print("type of x")
print(type(x))  # <class '__main__.Foo'>
print("type of Foo")
print(type(Foo))  # <class 'type'>


"""
The type of x is class Foo, as you would expect. But the type of Foo, the class itself, is type. 
In general, the type of any new-style class is type.

The type of the built-in classes you are familiar with is also type:
"""
print("type of built-in classes: int, float, dict, list, tuple")
for t in int, float, dict, list, tuple:
    print(type(t))  # <class 'type'>

"""
For that matter, the type of type is type as well (yes, really):
"""
print("type of 'type' class")
print(type(type))

"""
type is a metaclass, of which classes are instances. 
Just as an ordinary object is an instance of a class, any new-style class in Python, 
and thus any class in Python 3, is an instance of the type metaclass.

In the above case:

1) x is an instance of class Foo.
2) Foo is an instance of the type metaclass.
3) type is also an instance of the type metaclass, so it is an instance of itself.

"""