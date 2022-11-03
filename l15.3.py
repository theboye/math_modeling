import functools
from math import gcd

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [str(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"calling func {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"func {func.__name__} returned {value}")
        return value
 
    return wrapper_debug



@debug
def show_debug_function(terms):
    return gcd(terms,14)
 
show_debug_function(6666)