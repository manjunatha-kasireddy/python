def myfunc(n):
  return abs(n - 2)

thislist = ["c-lang", "java", "Python", "html", "css", "Javascript"]
thislist.sort()
print(thislist)
thislist2 = [10, 54, 5, 52, 23]
thislist2.sort(reverse = True)
print(thislist2)
thislist2.sort(key = myfunc)
print(thislist2)
thislist.sort(key = str.lower)
print(thislist)
thislist.reverse()
print(thislist)


