#Rewrite your pay computation to give employee 1.5 times the hourly rate for
#hours worked above 40 hours.
hour = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hour > 40:
    overtime = (hour - 40.0) * (0.5 * rate)
    regular = hour * rate
    pay = overtime + regular


else:
    pay = hour * rate

print("Pay: ", pay)
