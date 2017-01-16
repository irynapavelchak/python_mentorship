def decorator1(func):
    def function1(a, b):
        print "Arguments of function are:", a, b
        return func(a, b)
    return function1

@decorator1
def get_arguments(a, b):
    return "some result"

get_arguments("bbb1", "ffff1")
get_arguments(a = "bbb2", b = "ffff2")
