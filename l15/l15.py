"""
def decorator(func):
    def wrapper_function(*args, **kwargs):
        #print(*args, **kwargs)
        func(*args, **kwargs)
        print(args, **kwargs)
    return wrapper_function
 
 
@decorator
def greet(name,a = 10):
    print(f"Привет {name}!")
 
greet("Анастасия")
"""
"""
def logger(func):
    # def wrapper_function(*args, **kwargs):
    def wrapper_function(list_of_num):
        # result = func(*args, **kwargs)
        result = func(list_of_num)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapper_function
  
@logger
def summator(list_of_num):
    return sum(list_of_num)
 
print(summator([1,2,3,4]))
"""
"""
def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

	
@logger('file_log.txt')
def summator(list_of_num):
    return sum(list_of_num)
 
summator([1,2,3,4])
"""

