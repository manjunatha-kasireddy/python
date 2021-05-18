class college:
    def __init__(self, fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x = college("manjunatha", "reddy")
x.printname()
class Students(college):
  def __init__(self, fname, lname, year):
    super().__init__(fname,lname)
    self.sec = year
  def first(self):
    print("welcome",self.firstname,self.lastname,"to the class of",self.sec)
x = Students("teja","hari",2018)
x.printname()
print(x.sec)
x.first()