
name1 = input("What is the first name?")
while len(name1) < 1:
    print ("You didn't enter a name!")
    name1 = input("What is the first name?")

name2 = input("What is the second name?")
while len(name2) < 1:
    print ("You didn't enter a name!")
    name1 = input("What is the second name?")

name3 = input("What is the third name?")
while len(name3) < 1:
    print ("You didn't enter a name!")
    name1 = input("What is the third name?")
    
salary1 = input("What is " + str(name1) + "'s weekly income?")
while len(salary1) < 1 or salary1.isalpha():
    salary1 = input("What is " + str(name1) + "'s income?")
salary1 = float(salary1)
    
mortgage1 = input("What is " + str(name1) + "'s weekly mortgage expense?")
while len(mortgage1) < 1 or mortgage1.isalpha():
    mortgage1 = input("What is " + str(name1) + "'s weekly mortgage expense?")
mortgage1 = float(mortgage1)

grocery1 = input("What is " + str(name1) + "'s grocery expense?")
while len(grocery1) < 1 or grocery1.isalpha():
    grocery1 = input("What is " + str(name1) + "'s weekly grocery expense?")
grocery1 = float(grocery1)

power1 = input("What is " + str(name1) + "'s weekly power expense?")
while len(power1) < 1 or power1.isalpha():
    power1 = input("What is " + str(name1) + "'s weekly power expense?")
power1 = float(power1)

vehicle1 = input("What is your weekly vehicle expense?")
while len(vehicle1) < 1 or vehicle1.isalpha():
    vehicle1 = input("What is " + str(name1) + "'s weekly vehicle expense?")
vehicle1 = float(vehicle1)

weekly_expenses1 =  float(mortgage1 + grocery1 + power1 + vehicle1)
left_over1 = float(salary1 - weekly_expenses1)
needed_savings1 = float(salary1 * .1)

salary2 = input("What is " + str(name2) + "'s weekly income?")
while len(salary2) < 1 or salary2.isalpha():
    salary2 = input("What is " + str(name2) + "'s weekly income?")
salary2 = float(salary2)
    
mortgage2 = input("What is " + str(name2) + "'s mortgage expense?")
while len(mortgage2) < 1 or mortgage2.isalpha():
    mortgage2 = input("What is " + str(name2) + "'s weekly mortgage expense?")
mortgage2 = float(mortgage2)

grocery2 = input("What is " + str(name2) + "'s grocery expense?")
while len(grocery2) < 1 or grocery2.isalpha():
    grocery2 = input("What is " + str(name2) + "'s weekly grocery expense?")
grocery2 = float(grocery2)

power2 = input("What is " + str(name2) + "'s weekly power expense?")
while len(power2) < 1 or power2.isalpha():
    power2 = input("What is " + str(name2) + "'s weekly power expense?")
power2 = float(power2)

vehicle2 = input("What is your weekly vehicle expense?")
while len(vehicle2) < 1 or vehicle2.isalpha():
    vehicle2 = input("What is " + str(name2) + "'s weekly vehicle expense?")
vehicle2 = float(vehicle2)

weekly_expenses2 =  float(mortgage2 + grocery2 + power2 + vehicle2)
left_over2 = float(salary2 - weekly_expenses2)
needed_savings2 = float(salary2 * .1)

display_salary2 = format(salary2, ".2f")
display_weekly_expenses2 = format(weekly_expenses2, ".2f")
display_left_over2 = format(left_over2, ".2f")
display_needed_savings2 = format(needed_savings2, ".2f")

salary3 = input("What is " + str(name3) + "'s weekly income?")
while len(salary3) < 1 or salary3.isalpha():
    salary3 = input("What is " + str(name3) + "'s weekly income?")
salary3 = float(salary3)
    
mortgage3 = input("What is " + str(name3) + "'s mortgage expense?")
while len(mortgage3) < 1 or mortgage3.isalpha():
    mortgage3 = input("What is " + str(name3) + "'s weekly mortgage expense?")
mortgage3 = float(mortgage3)

grocery3 = input("What is " + str(name3) + "'s grocery expense?")
while len(grocery3) < 1 or grocery3.isalpha():
    grocery3 = input("What is " + str(name3) + "'s weekly grocery expense?")
grocery3 = float(grocery3)

power3 = input("What is " + str(name3) + "'s weekly power expense?")
while len(power3) < 1 or power3.isalpha():
    power3 = input("What is " + str(name3) + "'s weekly power expense?")
power3 = float(power3)

vehicle3 = input("What is your weekly vehicle expense?")
while len(vehicle3) < 1 or vehicle3.isalpha():
    vehicle3 = input("What is " + str(name3) + "'s weekly vehicle expense?")
vehicle3 = float(vehicle3)

weekly_expenses3 =  float(mortgage3 + grocery3 + power3 + vehicle3)
left_over3 = float(salary3 - weekly_expenses3)
needed_savings3 = float(salary3 * .1)

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

print ("")
print (name2.strip(), end = '')
print (":")
print ("----------------------------")
print ("Weekly Salary : $", end = '')
print (display_salary2)
print ("Weekly Expenses : $", end = '')
print (display_weekly_expenses2)
print ("Money Left Over : $", end = '')
print (display_left_over2)
print ("Money Needed to Save : $", end  = '')
print (display_needed_savings2)    


if left_over2 < needed_savings2:
    print ("")
    print (name2.strip(), "needs to save more money.")
else:
    print ("\nCongratulations,", name2, end  = '')
    print (", you are on your way to financial freedom!")

    
print ("")
print (name3.strip(), end = '')
print (":")
print ("----------------------------")
print ("Weekly Salary : $", end = '')
print (display_salary3)
print ("Weekly Expenses : $", end = '')
print (display_weekly_expenses3)
print ("Money Left Over : $", end = '')
print (display_left_over3)
print ("Money Needed to Save : $", end  = '')
print (display_needed_savings3)    


if left_over3 < needed_savings3:
    print ("")
    print (name3.strip(), "needs to save more money.")
else:
    print ("\nCongratulations,", name3, end  = '')
    print (", you are on your way to financial freedom!")
