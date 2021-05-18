class MyClass:
    x = 41


new = MyClass()
print(new.x)


class newclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


new3 = newclass("teja", 21)
new3.myfunc()

class second:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello to class  " + abc.name)


s1 = second("manju", 21)
s1.myfunc()
s1.age = 22
print(s1.age)
del s1.age
del s1
print(s1)