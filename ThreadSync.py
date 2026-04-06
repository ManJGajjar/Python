import threading

counter = 10

def increment(theLock, N):
   global counter
   for i in range(N):
      theLock.acquire()
      counter += 1
      theLock.release()

lock = threading.Lock()
t1 = threading.Thread(target=increment, args=[lock, 2])
t2 = threading.Thread(target=increment, args=[lock, 10])
t3 = threading.Thread(target=increment, args=[lock, 4])

t1.start()
t2.start()
t3.start()

for thread in (t1, t2, t3):
   thread.join()

print("All threads have completed")
print("The Final Counter Value:", counter)