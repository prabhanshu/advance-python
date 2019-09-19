
# Add all students to course
# for student in students:
#     student.enroll(course)  # Must be active


def factorial(n: int) -> int:
    """Recursive factorial

    Recursively compute a factorial
    :param n: the integer to compute the factorial
    """
    if n == 2:
        return 2
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print(factorial(5))


# Comments mentioned after function is called "Docstring" and can be accessed by: >>> help(factorial) in python shell

# Hold Option key and use left click to select multiple cursor while typing same comment on multiple line

def a():
    """This is a docstring"""
    pass


def b():
    """This is a docstring"""
    pass


def c():
    """This is a docstring"""
    pass

