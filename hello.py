print("hello")
def fun1(a):
    """this is a doc string of func1"""
    print(a)
    return a
print(fun1.__doc__)
print(fun1(5))
