thistuple = ("c-lang", "java", "python", "html", "css", "javascript")
y = list(thistuple)
y.remove("c-lang")
thistuple = tuple(y)
print(thistuple)
y = list(thistuple)
y.append("c++")
thistuple = tuple(y)
print(thistuple)
del thistuple
print(thistuple)