class test:
   def __init__(self):
      self.name = "Man"
      
obj = test()
setattr(obj, "age", 20)
setattr(obj, "name", "Mann")
print (obj.name, obj.age)