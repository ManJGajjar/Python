class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Peter Griffin"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))