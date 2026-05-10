class InvalidAgeError(Exception):
   def __init__(self, age, message="Age must be between 18 and 100"):
      self.age = age
      self.message = message
      super().__init__(self.message)

   def __str__(self):
     return f"{self.message}. Provided age: {self.age}"

def set_age(age):
   if age < 18 or age > 100:
      raise InvalidAgeError(age)
   print(f"Age is set to {age}")

try:
   set_age(150)
except InvalidAgeError as e:
   print(f"Invalid age: {e.age}. {e.message}")