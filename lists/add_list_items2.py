thislist = ["c-lang", "java"]
thislist2 = ["python", "html", "css", "javascript"]
thislist.append("xml")
print(thislist)
thislist.insert(1, "c++")
print(thislist)
thislist.extend(thislist2)
print(thislist)
thistuple = ("class", "object")
thislist.extend(thistuple)
print(thislist)