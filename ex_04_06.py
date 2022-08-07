#Rewite your pay computation with time-and-a-half for overtime and create
#a function called computepay which takes teo parameters (hours $ rate)
def computepay(hours, rate):
    #print("In computepay", hours, rate)
    if hour > 40:
        overtime = (hours - 40.0) * (0.5 * rate)
        regular = hours * rate
        pay = overtime + regular

    else:
        pay = hour * rate

    return pay

hour = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = computepay(hour,rate)

print("Pay: ", pay)
