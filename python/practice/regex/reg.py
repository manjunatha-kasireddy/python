import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
  
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


'Hello how r you! are you ok? call me at 965847 '

Task 1
you!
ok?

import re
txt = "Hello how r you! are you ok? call me at 965847"
x = re.findall("you!")



Task 2
965847