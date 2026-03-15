class test:
   def __init__(self):
      self.name = "Man"
      
obj = test()
print (getattr(obj, "name"))