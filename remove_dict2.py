thisdict = {"branch": "cse","course":"java","rno":41 }
thisdict.pop("course")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict["branch"]
print(thisdict)
thisdict.clear()
print(thisdict)