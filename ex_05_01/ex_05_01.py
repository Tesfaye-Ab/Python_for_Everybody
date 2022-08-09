#Write a program which repeatedly reads numbers until the user enters "done".
#Once "done" is entered, print out the total, count, and average of the numbers.
#If the user enters anything other than a number, detect their mistake using
#try and except and print an error message and skip to the next numbers

num = 0 # running count
tot = 0.0 # running total

while True:
    user_val = input('Enter a number:')
    if user_val == 'done': # if the user enters "done", break out of the loop
        break
    try: # if the user enters a string other than "done", break but go back 
        fval = float(user_val) # convert the input string to floating number
    except:
        print('Invalid input')
        continue
    #print(fval)
    num = num + 1 # counts the input numbers
    tot = tot + fval # calculate the total of the inputs

#print('All DONE')
print(tot, num, tot/num)
