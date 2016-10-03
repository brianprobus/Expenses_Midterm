name1 = input("What is the first name?")
while len(name1) < 1:
    print ("You didn't enter a name!")
    name1 = input("What is the first name?")
    
salary1 = input("What is " + str(name1) + "'s weekly income?")
while len(salary1) < 1 or salary1.isalpha():
    salary1 = input("What is your weekly income?")
salary1 = float(salary1)
    
mortgage1 = input("What is " + str(name1) + "'s mortgage expense?")
while len(mortgage1) < 1 or mortgage1.isalpha():
    mortgage1 = input("What is your weekly mortgage expense?")
mortgage1 = float(mortgage1)

grocery1 = input("What is " + str(name1) + "'s grocery expense?")
while len(grocery1) < 1 or grocery1.isalpha():
    grocery1 = input("What is your weekly grocery expense?")
grocery1 = float(grocery1)

power1 = input("What is " + str(name1) + "'s weekly power expense?")
while len(power1) < 1 or power1.isalpha():
    power1 = input("What is your weekly power expense?")
power1 = float(power1)

vehicle1 = input("What is your weekly vehicle expense?")
while len(vehicle1) < 1 or vehicle1.isalpha():
    vehicle1 = input("What is your weekly vehicle expense?")
vehicle1 = float(vehicle1)

weekly_expenses1 =  float(mortgage1 + grocery1 + power1 + vehicle1)
left_over1 = float(salary1 - weekly_expenses1)
needed_savings1 = float(salary1 * .1)



display_salary1 = format(salary1, ".2f")
display_weekly_expenses1 = format(weekly_expenses1, ".2f")
display_left_over1 = format(left_over1, ".2f")
display_needed_savings1 = format(needed_savings1, ".2f")

print ("")
print (name1.strip(), end = '')
print (":")
print ("----------------------------")
print ("Weekly Salary : $", end = '')
print (display_salary1)
print ("Weekly Expenses : $", end = '')
print (display_weekly_expenses1)
print ("Money Left Over : $", end = '')
print (display_left_over1)
print ("Money Needed to Save : $", end  = '')
print (display_needed_savings1)    


if left_over1 < needed_savings1:
    print ("")
    print (name1.strip(), "needs to save more money.")
else:
    print ("\nCongratulations,", name1, end  = '')
    print (", you are on your way to financial freedom!")


