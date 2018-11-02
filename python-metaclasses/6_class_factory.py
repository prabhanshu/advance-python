"""
In the same way that a class functions as a template for the creation of objects,
a metaclass functions as a template for the creation of classes.
Metaclasses are sometimes referred to as class factories.

Compare the following two examples:
"""


# Object Factory
class Foo:
    def __init__(self):
        self.attr = 100


x = Foo()
print(x.attr)  # 100

y = Foo()
print(y.attr)  # 100

z = Foo()
print(z.attr)  # 100


# Class Factory
class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100


class X(metaclass=Meta):
    pass


print(X.attr)  # 100


class Y(metaclass=Meta):
    pass


print(Y.attr)  # 100


class Z(metaclass=Meta):
    pass


print(Z.attr)  # 100


