# tech201_controlflow

# Control flow

- control flow -> flow through a particular decision process.

- if statement

 `age =19`

`film_rating = "universal"`

`if film_rating.lower() == "universal":`
    `print("All age groups can watch this film.")`

`elif film_rating.lower() == "pg":`
     `print("General viewing but parental guidance advised.")`

`elif film_rating.lower() == "12" or film_rating == "12a":`
   `print("12 rated movies may not be suitable for for those under 12, supervision is recommended.")

`elif film_rating.lower() == "15":`
    `print("Must be 15 to watch")`

`elif film_rating.lower() == "18":`
    `print("You must be 18 to watch this.")`

`else:
    print("This is not a correct rating please use universal, pg, 12, 15, 18")`

In Python there are no 'switch statements' or 'case statements'.
