i = lambda x, y, z : z + x + y
print(i(10, 20, 30 ))
def firfun(a):
  return lambda i : i * a
new = firfun(10)
print(new(20))