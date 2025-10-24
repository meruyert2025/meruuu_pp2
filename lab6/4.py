import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  # time.sleep принимает секунды, поэтому делим на 1000
    return math.sqrt(number)

number = 25100
delay = 2123
result = delayed_sqrt(number, delay)
print("Square root of", number, "after", delay, "milliseconds is", result)
