# Tech201_controlflow

## Control flow



- control flow -> flow through a particular decision process.

- if statement

- if statements are some of the most important statements used in python, they are needed to tell the program to take a certain action after conditionals.

- Here we have set the variable age as 19.

 `age =19`
- Usually we would ask for an input but we are using this as an example.
- So now the age is 19 it will tell us which movies we are eligible to watch.
`film_rating = "universal"`

`if film_rating.lower() == "universal":`
    `print("All age groups can watch this film.")`

- Depending on the age the if statement will move on to the next statement or next condition and so on and forth until none of the conditions are met and it will go to the `else` statement.

- The `elif` keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

`elif film_rating.lower() == "pg":`
     `print("General viewing but parental guidance advised.")`

`elif film_rating.lower() == "12" or film_rating == "12a":`
   `print("12 rated movies may not be suitable for for those under 12, supervision is recommended.")`

`elif film_rating.lower() == "15":`
    `print("Must be 15 to watch")`
- Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

1. If indentations are not used an error will occur.

`elif film_rating.lower() == "18":`
    `print("You must be 18 to watch this.")`

`else:
    print("This is not a correct rating please use universal, pg, 12, 15, 18")`

- The `else` keyword catches anything which isn't caught by the preceding conditions.
- If all fails it will print this out above:

In Python there are no 'switch statements' or 'case statements'.
