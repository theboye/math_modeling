
def decorator(func):
  def wrapped(*args,**kwargs):
    a = func(*args)[0]
    b = func(*args)[1]
    c = func(*args)[-1]
    if c == '-':
      result = a-b
    if c == '+':
      result = a+b
    if c == '*':
      result = a*b
    if c == '/':
      if b != 0:
        result = a/b
    
   
    return result
  return wrapped

@decorator
def two_variables(*args):
  return args
  
print(two_variables(90,3,'-'))