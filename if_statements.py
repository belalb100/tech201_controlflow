# Control flow

#control flow -> flow through a particular decision process.

# if statement

# age =19

film_rating = "universal"

if film_rating.lower() == "universal":
    print("Al age groups can watch this film.")
elif film_rating.lower() == "pg":
    print("General viewing but parental guidance advised.")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for for those under 12, supervision is recommended.")
elif film_rating.lower() == "15":
    print("Must be 15 to watch")
elif film_rating.lower() == "18":
    print("You must be 18 to watch this.")
else:
    print("This is not a correct rating please use universal, pg, 12, 15, 18")

# In Python there are no 'switch statements' or 'case statements'.



# if age >= 18:
#     print("You are the correct age to watch the film and can buy a ticket")
# elif age <18:
#     print("I'm afraid you aren't old enough.")

