#FIZZBUZZ

# import random
#
# for i in range(1, 101):
#     num = random.randint(1, 100)
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
#
# print("Program complete.")

import random

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def run_fizz_buzz(n):
    for i in range(1, n + 1):
        num = random.randint(1, 100)
        result = fizz_buzz(num)
        print(result)

run_fizz_buzz(101)

print("Program complete.")

