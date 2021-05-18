import module
module.greeting("Jonathan")

import module
a = module.person1["age"]
print(a)

import module as mx
a = mx.person1["age"]
print(a)

import platform
x = platform.system()
print(x)

import platform
x = dir(platform)
print(x)

from module import person1
print (person1["age"])
