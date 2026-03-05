def getA(self):
   return self.a
obj = type('',(object,),{'a':5,'b':6,'c':7,'getA':getA,'getB':lambda self : self.b})()
print (obj.getA(), obj.getB())