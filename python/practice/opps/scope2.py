def ffunc():
  x = 10
  print(x)
ffunc()
def myfunc():
  x = 541
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()

x = 596
def myfunc():
  print(x)
myfunc()
print(x)

x = 415
def myfunc():
  x = 425
  print(x)
myfunc()
print(x)

def myfunc():
  global x
  x = 500
myfunc()
print(x)

x = 554
def myfunc():
  global x
  x = 596
myfunc()
print(x)
