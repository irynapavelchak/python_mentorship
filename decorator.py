def decorator1(func):
    def function1(*args, **kwargs):
        print "Arguments of function are:"
        for arg in args:
            print arg
        for key in kwargs:
            print key, ":", kwargs[key]                
        return func(*args, **kwargs)
    return function1

@decorator1
def get_arguments(*args, **kwargs):
    return "some result"

get_arguments("bbb1", "ffff1")
get_arguments(a = "bbb2", b = "ffff2")
