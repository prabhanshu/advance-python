# Explicit Code
# In the good code above, x and y are explicitly received from the caller, and an explicit dictionary is returned.
# The developer using this function knows exactly what to do by reading the first and last lines,
# which is not the case with the bad example.


def make_complex_bad(*args):
    x, y = args
    return dict(**locals())


def make_complex_good(x, y):
    return {'x': x, 'y': y}


# One statement per line
# While some compound statements such as list comprehensions are allowed and appreciated for their brevity and
# their expressiveness, it is bad practice to have two disjointed statements on the same line of code.

# Bad
# print('one');print('two')
#
# if x == 1:
#     print('one')
#
# if < complex comparison > and < other complex comparison >:
#     # do something

# Good
# print 'one'
# print 'two'
#
# if x == 1:
#     print 'one'
#
# cond1 = <complex comparison>
# cond2 = <other complex comparison>
# if cond1 and cond2:
#     # do something

