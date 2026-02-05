class MyNumbers:
  def _iter_(self):
    self.a = 1 
    return self 
  
  def _next_(self):
    x = self.a
    self.a += 1 
    return x 
  
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))