import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_sum(a, b):
   logging.debug(f"Calculating sum of {a} and {b}")
   result = a + b
   logging.info(f"Sum calculated successfully: {result}")
   return result

if __name__ == "__main__":
   logging.info("Starting the program")
   result = calculate_sum(10, 20)
   logging.info("Program completed")