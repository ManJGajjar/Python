import array as arr

a = arr.array('i', [1, 2, 3])
print (type(a), a)

a = arr.array('u', 'BAT')
print (type(a), a)

a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)