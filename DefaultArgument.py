def percent(phy, maths, maxmarks=200):
   val = (phy + maths) * 100/maxmarks
   return val

phy = 60
maths = 70

result = percent(phy, maths)
print ("percentage:", result)

phy = 40
maths = 46
result = percent(phy, maths, 100)
print ("percentage:", result)