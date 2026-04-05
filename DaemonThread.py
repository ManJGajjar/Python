import threading 
from time import sleep

def run():
   thread = threading.current_thread()
   print(f'Daemon thread: {thread.daemon}')

thread = threading.Thread(target=run, daemon=True)

thread.start()

print('Is Main Thread is Daemon thread:', threading.current_thread().daemon)

sleep(0.5)