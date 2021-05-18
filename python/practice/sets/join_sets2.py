myset = {"c-lang",'java',"html"}
my = {"c++","css","python" ,"html"}
set1 = myset .union(my)
print(set1)
myset .update(my)
print(myset)
myset2 = {"c-lang",'java',"html","xml"}
my2 = {"c-lang","css","python" ,"html"}
myset2.intersection_update(my2)
print(myset2)
set2 = myset2.intersection(my2)
print(set2)
myset3 = {"c-lang",'java',"html","xml"}
my3 = {"c-lang","css","python" ,"html"}
myset3.symmetric_difference_update(my3)
print(myset3)
set3 = myset3.symmetric_difference(my3)
print(myset3)