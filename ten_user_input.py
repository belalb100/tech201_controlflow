# While loop

# amount = 0
# number = 0
#
# while True:
#     number += int(input("Number:"))  # Getting users input and turning it into a int and adding it to the current value of that number
#     amount += 1 #Going up by 1 each time a user puts an input.
#     if amount == 10:
#         break
#
# print(f"Numbers in total:{amount}")
# print(f"Sum of numbers: {number}")
# print(number)





# For loop

total = 0
for i in range(10): #In built function. it esentially automatically makes a list based on the number you put in.
    total += int(input("Enter a Number."))

print(f"The total of your input is: {total}")

