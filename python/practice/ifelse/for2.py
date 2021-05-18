ex = ["c-lang", "java", "python", "html",  "javascript"]
for x in ex:
  print(x)
for x in "java":
  print(x)
for x in ex:
  print(x)
  if x == "python":
    break
for x in ex:
  if x == "html":
    break
  print(x)
for x in ex:
  if x == "c-lang":
    continue
  print(x)
for x in range(6):
  print(x)
for x in range(2, 6):
  print(x)
for x in range(2, 30, 3):
  print(x)
for x in range(6):
  print(x)
else:
  print("Finally finished!")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
adj = ["red", "big", "tasty"]
for x in adj:
  for y in ex:
    print(x, y)