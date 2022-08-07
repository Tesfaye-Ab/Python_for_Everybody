#Rewrite your pay program using 'try' and 'except' so that your program handles
#non-numeric input gracefully by printing a message and exiting the program.
try:
    hour = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

if hour > 40:
    overtime = (hour - 40.0) * (0.5 * rate)
    regular = hour * rate
    pay = overtime + regular


else:
    pay = hour * rate

print("Pay: ", pay)
