thisset = {"c-lang",'java',"html","python"}
thisset.remove("java")
print(thisset)
thisset.discard("python")
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
thisset.clear()
print(thisset)
del thisset
print(thisset)
