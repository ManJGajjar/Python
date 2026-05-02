try:
   open("nofile.txt")
except OSError:
   raise RuntimeError("unable to handle error")