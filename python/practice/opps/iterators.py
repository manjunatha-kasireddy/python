
import json
x = { 
     "name":"John", 
     "age":30, 
     "city":[
       {
        "name":"New York",
        "pincode": '500020'        
     },
    {
        "name":"HYD York",
        "pincode": '500020'        
     }
     ]
}
# y = json.loads(x)
print(x["city"][1]["name"])

# print(y.items())

# print(type(x))
# print(type(y))



# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"

# for x in mystr:
#   print(x)

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
