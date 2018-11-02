"""
Consider again this well-worn example:
"""


class Foo:
    pass


f = Foo()
print(f)


"""
The expression Foo() creates a new instance of class Foo. 
When the interpreter encounters Foo(), the following occurs:

    1) The __call__() method of Foo’s parent class is called. 
        Since Foo is a standard new-style class, its parent class is the type metaclass, 
        so type’s __call__() method is invoked.

    2) That __call__() method in turn invokes the following:
        a) __new__()
        b) __init__()
        
If Foo does not define __new__() and __init__(), default methods are inherited from Foo’s ancestry. 
But if Foo does define these methods, they override those from the ancestry, 
which allows for customized behavior when instantiating Foo.

In the following, a custom method called new() is defined and assigned as the __new__() method for Foo:
"""


def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new
f = Foo()
print(f.attr)  # 100

g = Foo()
print(g.attr)  # 100


"""
This modifies the instantiation behavior of class Foo: each time an instance of Foo is created, 
by default it is initialized with an attribute called attr, which has a value of 100. 
(Code like this would more usually appear in the __init__() method and not typically in __new__(). 
This example is contrived for demonstration purposes.)
"""


"""
Now, as has already been reiterated, classes are objects too. 
Suppose you wanted to similarly customize instantiation behavior when creating a class like Foo. 
If you were to follow the pattern above, you’d again define a custom method and assign 
it as the __new__() method for the class of which Foo is an instance. 
Foo is an instance of the type metaclass, so the code looks something like this:
"""


# Spoiler alert:  This doesn't work!
def new(cls):
    x = type.__new__(cls)
    x.attr = 100
    return x

# uncomment below line to test if it works or not
# type.__new__ = new

"""
Except, as you can see, you can’t reassign the __new__() method of the type metaclass. Python doesn’t allow it.

This is probably just as well. type is the metaclass from which all new-style classes are derived. 
You really shouldn’t be mucking around with it anyway. 
But then what recourse is there, if you want to customize instantiation of a class?

One possible solution is a custom metaclass. 
Essentially, instead of mucking around with the type metaclass, you can define your own metaclass, 
which derives from type, and then you can muck around with that instead.

The first step is to define a metaclass that derives from type, as follows:
"""


class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

"""
The definition header class Meta(type): specifies that Meta derives from type. 
Since type is a metaclass, that makes Meta a metaclass as well.

Note that a custom __new__() method has been defined for Meta. 
It wasn’t possible to do that to the type metaclass directly. 
The __new__() method does the following:
    1) Delegates via super() to the __new__() method of the parent metaclass (type) to actually create a new class
    2) Assigns the custom attribute attr to the class, with a value of 100
    3) Returns the newly created class
    
Now the other half of the voodoo: Define a new class Foo and specify that its metaclass is the custom metaclass Meta, 
rather than the standard metaclass type. This is done using the metaclass keyword in the class definition as follows:
"""


class Foo(metaclass=Meta):
    pass


print(Foo.attr)  # 100


# Any other classes you define similarly will do likewise
class Bar(metaclass=Meta):
    pass


class Qux(metaclass=Meta):
    pass


print(Foo.attr, Bar.attr, Qux.attr)  # 100 100 100
