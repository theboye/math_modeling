def boba(num1):
  def decorator(func):
    def wrapped(*args,**kwargs):
      result = num1+ func(*args)
      print(result)
      return result
    return wrapped
  return decorator

@boba(6)
def summator(a):
  return a

summator(9)