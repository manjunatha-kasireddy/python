thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(thisdict)
x = thisdict.get("model")
print(thisdict)
x = thisdict.keys()
print(thisdict)
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1969
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change