list1 = ["c-lang", "java", "Python"]
list2 = ["html", "css", "Javascript"]
list1.extend(list2)
print(list1)
for x in list2:
  list1.append(x)
print(list1)
