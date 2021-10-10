class Rectangle:
         def __init__(self, width, height, sign):
                  self.w = int(width)
                  self.h = int(height)
                  self.s = str(sign)
         def __str__(self):
                  rect = []
                  for i in range(self.h):
                           rect.append(self.s * self.w)

                  rect = '\n'.join(rect) # возвращяет строку, разделённую \n из элементов списка
                  return rect

b = Rectangle(10, 5, 'C')
print(b)
