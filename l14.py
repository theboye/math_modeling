'''class Ball:

  pass

ball_1 = Ball()
ball_2 = Ball()
'''


class Point:
  def __init__(self,x0,y0):
    self.x = x0
    self.y = y0
    def __str__(self):
      return f'Point: {self.x},{self.y}'

    def move(self,dx,dy):
      self.x += dx
      self.y += dy
      
p = Point(5,9)
print(p)
p.move(5,-3)
print(p)