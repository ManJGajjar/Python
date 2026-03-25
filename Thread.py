from threading import Thread

def addition_of_numbers(x, y):
   result = x + y
   print('Addition of {} + {} = {}'.format(x, y, result))

def cube_number(i):
   result = i ** 3
   print('Cube of {} = {}'.format(i, result))

def basic_function():
   print("Basic function is running concurrently...")

Thread(target=addition_of_numbers, args=(2, 4)).start()  
Thread(target=cube_number, args=(4,)).start() 
Thread(target=basic_function).start()