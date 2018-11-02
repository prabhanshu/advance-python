"""
Is This Really Necessary?
As simple as the class factory example is, it is the essence of how metaclasses work.
They allow customization of class instantiation.

Still, this is a lot of fuss just to bestow the custom attribute attr on each newly created class.
Do you really need a metaclass just for that?

In Python, there are at least a couple other ways in which effectively the same thing can be accomplished:
"""


# Simple Inheritance
class Base:
    attr = 100


class X(Base):
    pass


class Y(Base):
    pass


class Z(Base):
    pass


print(X.attr)  # 100
print(Y.attr)  # 100
print(Z.attr)  # 100


# Class Decorator

def decorator(cls):
    class NewClass(cls):
        attr = 100
    return NewClass


@decorator
class X:
    pass


@decorator
class Y:
    pass


@decorator
class Z:
    pass


print(X.attr)  # 100
print(Y.attr)  # 100
print(Z.attr)  # 100


"""
CONCLUSION:
As Tim Peters suggests, metaclasses can easily veer into the realm of being a “solution in search of a problem.” 
It isn’t typically necessary to create custom metaclasses. 
If the problem at hand can be solved in a simpler way, it probably should be. 
Still, it is beneficial to understand metaclasses so that you understand Python classes in general and 
can recognize when a metaclass really is the appropriate tool to use.
"""