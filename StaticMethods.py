class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
 
   def showcount():
      print (Employee.empCount)
      return
   counter = staticmethod(showcount)

e1 = Employee("Peter", 24)
e2 = Employee("Quagmire", 26)
e3 = Employee("Cleveland", 27)

e1.counter()
Employee.counter()