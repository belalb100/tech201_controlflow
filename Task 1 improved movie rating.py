while True:
    age = int(input("Please enter your age: "))

    if age < 1 or age > 117:
        print("Invalid age entered. Please enter your age again.")
    else:
        break
if age >= 18:
    print("You can watch U, PG, 12, 15 and 18 rated movies.")
elif age >= 15:
    print("You can watch U, PG, 12, 15 rated movies.")
elif age >= 12:
    print("You can watch U, PG and 12 rated movies.")
else:
    print("You can watch U and PG rated movies.")
