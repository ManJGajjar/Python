def intr(amt, rate, /):
   val = amt * rate / 100
   return val
   
print(intr(amt=1000, rate=10))