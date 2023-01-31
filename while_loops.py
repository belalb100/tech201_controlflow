# While loops

#Quite limited but quite specific as a tool.

# While loops monitor data rather than iterate.

# x = 0
#
# while x < 10: # BEING USED as a Comparison. Comaprison operator. How does x compare to 10 is it smaller than 10.
#     print(f"it's working -> {x}")
#     x += 3 #inreamenter

# We will now use a break.

# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break # Gets you completed out of the while loop at that point.
#     x += 1
# print(x)

# We can use while loops to verify user input

# Asking for someone's age
# This can either be and in(20) or string (twenty)

# age = input("What is you age?")
#
# print(f"your age is {age}")

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) <117:
        user_prompt = False
    else:
        print("Please provide your answer in digits and below 117.")

print(f"Your age is {age}")


