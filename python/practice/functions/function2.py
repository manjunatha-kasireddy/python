def ffunction():
  print("first function")
ffunction()
def sfunction(fname):
  print(fname + " cse ")
sfunction("manju")
sfunction("teja")
sfunction("sirish")
def my_function(*studs):
  print("The students are: " + studs[0])
my_function("sirish", "Teja", "manju")
def tri_recursion(i):
  if(i > 0):
    result = i + tri_recursion(i - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)
