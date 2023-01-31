#First if Statement Task, Weekly pay:

hours_worked = float(input("Please enter the number of hours worked this week: "))
rate_of_pay = float(input("Please enter your hourly rate of pay: "))

if hours_worked <= 40:
    gross_pay = hours_worked * rate_of_pay
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (rate_of_pay * 1.5)
    gross_pay = (40 * rate_of_pay) + overtime_pay

print("Your total earnings for this week are:", gross_pay)
