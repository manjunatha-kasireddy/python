thislist = ["c-lang", "java", "python", "html", "css", "javascript"]    
newlist = [i for i in thislist if "a" in i]
print(newlist)
newlist = [i for i in thislist if i == "python"]
print(newlist)
newlist = [a if a == "c-lang" else "java" for a in thislist]
print(newlist)
newlist = ['hello' for b in thislist]
print(newlist)