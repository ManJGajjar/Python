from enum import Enum

class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   SCIENCE = 3
   SANSKRIT = 4

obj = subjects.MATHS
print (type(obj))