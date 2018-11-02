"""
In each of the following examples, the top snippet defines a class dynamically with type(),
while the snippet below it defines the class the usual way, with the class statement.
In each case, the two snippets are functionally equivalent.



EXAMPLE 1:
In this first example, the <bases> and <dct> arguments passed to type() are both empty.
No inheritance from any parent class is specified, and nothing is initially placed in the namespace dictionary.
This is the simplest class definition possible:
"""

# class dynamically created with type()
Foo = type('Foo', (), {})
x = Foo()
print(x)  # <__main__.Foo object at 0x04CFAD50>


# Usual way with class statement
class Foo:
    pass


x = Foo()
print(x)  # <__main__.Foo object at 0x0370AD50>

"""
EXAMPLE 2:
Here, <bases> is a tuple with a single element Foo, specifying the parent class that Bar inherits from. 
An attribute, attr, is initially placed into the namespace dictionary:
"""

# class dynamically created with type()
Bar = type('Bar', (Foo,), dict(attr=100))
x = Bar()
print(x.attr)  # 100
print(x.__class__)  # <class '__main__.Bar'>
print(x.__class__.__bases__)  # (<class '__main__.Foo'>,)


# Usual way with class statement
class Bar(Foo):
    attr = 100


x = Bar()
print(x.attr)  # 100
print(x.__class__)  # <class '__main__.Bar'>
print(x.__class__.__bases__)  # (<class '__main__.Foo'>,)


"""
EXAMPLE 3:
This time, <bases> is again empty. Two objects are placed into the namespace dictionary via the <dct> argument. 
The first is an attribute named attr and the second a function named attr_val, which becomes a method of the defined   
class:
"""

# class dynamically created with type()
Foo3 = type('Foo3', (), {
    'attr': 1000,
    'attr_val': lambda x3: x3.attr
})
x3 = Foo3()
print(x3.attr)  # 1000
print(x3.attr_val())  # 1000


# Usual way with class statement
class Foo3:
    attr = 1000

    def attr_val(self):
        return self.attr


x3 = Foo3()
print(x3.attr)  # 1000
print(x3.attr_val())  # 1000


"""
EXAMPLE 4:
Only very simple functions can be defined with lambda in Python. 
In the following example, a slightly more complex function is defined externally 
then assigned to attr_val in the namespace dictionary via the name f:
"""


# class dynamically created with type()
def f(obj):
    print("attr =", obj.attr)


Foo4 = type('Foo4', (), {
    'attr': 500,
    'attr_val': f
})

x4 = Foo4()
print(x4.attr)  # 500
print(x4.attr_val())  # attr = 500


# Usual way with class statement
def f(obj):
    print("attr =", obj.attr)


class Foo4:
    attr = 500
    attr_val = f


x4 = Foo4()
print(x4.attr)  # 500
print(x4.attr_val())  # 500



