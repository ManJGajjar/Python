class Parent: 
   def parentMethod(self):
      print ("Calling parent method")

class Child(Parent): 
   def childMethod(self):
      print ("Calling child method")

c = Child()
c.childMethod()
c.parentMethod() 