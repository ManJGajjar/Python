class student:
   def __init__(self):
      self.name = "Ashish"
      self.subs = self.subjects()
      return
   def show(self):
      print ("Name:", self.name)
      self.subs.display()
   class subjects:
      def __init__(self):
         self.sub1 = "Phy"
         self.sub2 = "Che"
         return
      def display(self):
         print ("Subjects:",self.sub1, self.sub2)
         
s1 = student()
s1.show()