#FIZZBUZZ

import random

for i in range(1, 101):
    num = random.randint(1, 100)
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print("Program complete.")
