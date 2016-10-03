#Print out what the program will do
print ("This program will take three names, and their incomes and expenses, ")
print ("then tell you if they are saving enough money every week!")

#Get 3 names from user and validate input
print ("")
name1 = input("What is the first name?")
while len(name1) < 1:
    print ("You didn't enter a name!")
    name1 = input("What is the first name?")

print ("")
name2 = input("What is the second name?")
while len(name2) < 1:
    print ("You didn't enter a name!")
    name2 = input("What is the second name?")

print ("")
name3 = input("What is the third name?")
while len(name3) < 1:
    print ("You didn't enter a name!")
    name3 = input("What is the third name?")

#Get name1's salary information
print ("")    
salary1 = input("What is " + str(name1) + "'s weekly income?")
while len(salary1) < 1 or salary1.isalpha():
    print ("That's not a valid input. Please enter a number!")
    salary1 = input("What is " + str(name1) + "'s weekly income?")
salary1 = float(salary1)

#Get name 1's expense information
mortgage1 = input("What is " + str(name1) + "'s weekly mortgage expense?")
while len(mortgage1) < 1 or mortgage1.isalpha():
    print ("That's not a valid input. Please enter a number!")
    mortgage1 = input("What is " + str(name1) + "'s weekly mortgage expense?")
mortgage1 = float(mortgage1)

grocery1 = input("What is " + str(name1) + "'s weekly grocery expense?")
while len(grocery1) < 1 or grocery1.isalpha():
    print ("That's not a valid input. Please enter a number!")
    grocery1 = input("What is " + str(name1) + "'s weekly grocery expense?")
grocery1 = float(grocery1)

power1 = input("What is " + str(name1) + "'s weekly power expense?")
while len(power1) < 1 or power1.isalpha():
    print ("That's not a valid input. Please enter a number!")
    power1 = input("What is " + str(name1) + "'s weekly power expense?")
power1 = float(power1)

vehicle1 = input("What is your weekly vehicle expense?")
while len(vehicle1) < 1 or vehicle1.isalpha():
    print ("That's not a valid input. Please enter a number!")
    vehicle1 = input("What is " + str(name1) + "'s weekly vehicle expense?")
vehicle1 = float(vehicle1)

#Add expenses together for total expenses
weekly_expenses1 =  float(mortgage1 + grocery1 + power1 + vehicle1)
#Subtract expenses from income for left over amount
left_over1 = float(salary1 - weekly_expenses1)
#Give needed savings a value (10%)
needed_savings1 = float(salary1 * .1)

#Format displayed amounts to give 2 decimal places
display_salary1 = format(salary1, ".2f")
display_weekly_expenses1 = format(weekly_expenses1, ".2f")
display_left_over1 = format(left_over1, ".2f")
display_needed_savings1 = format(needed_savings1, ".2f")

#Get name2's salary information
print ("")
salary2 = input("What is " + str(name2) + "'s weekly income?")
while len(salary2) < 1 or salary2.isalpha():
    print ("That's not a valid input. Please enter a number!")
    salary2 = input("What is " + str(name2) + "'s weekly income?")
salary2 = float(salary2)

#Get name 2's expense information
mortgage2 = input("What is " + str(name2) + "'s weekly mortgage expense?")
while len(mortgage2) < 1 or mortgage2.isalpha():
    print ("That's not a valid input. Please enter a number!")
    mortgage2 = input("What is " + str(name2) + "'s weekly mortgage expense?")
mortgage2 = float(mortgage2)

grocery2 = input("What is " + str(name2) + "'s weekly grocery expense?")
while len(grocery2) < 1 or grocery2.isalpha():
    print ("That's not a valid input. Please enter a number!")
    grocery2 = input("What is " + str(name2) + "'s weekly grocery expense?")
grocery2 = float(grocery2)

power2 = input("What is " + str(name2) + "'s weekly power expense?")
while len(power2) < 1 or power2.isalpha():
    print ("That's not a valid input. Please enter a number!")
    power2 = input("What is " + str(name2) + "'s weekly power expense?")
power2 = float(power2)

vehicle2 = input("What is your weekly vehicle expense?")
while len(vehicle2) < 1 or vehicle2.isalpha():
    print ("That's not a valid input. Please enter a number!")
    vehicle2 = input("What is " + str(name2) + "'s weekly vehicle expense?")
vehicle2 = float(vehicle2)

#Add expenses together for total expenses
weekly_expenses2 =  float(mortgage2 + grocery2 + power2 + vehicle2)
#Subtract expenses from income for left over amount
left_over2 = float(salary2 - weekly_expenses2)
#Give needed savings a value (10%)
needed_savings2 = float(salary2 * .1)

#Format displayed amounts to give 2 decimal places
display_salary2 = format(salary2, ".2f")
display_weekly_expenses2 = format(weekly_expenses2, ".2f")
display_left_over2 = format(left_over2, ".2f")
display_needed_savings2 = format(needed_savings2, ".2f")

#Get name3's salary information
print ("")
salary3 = input("What is " + str(name3) + "'s weekly income?")
while len(salary3) < 1 or salary3.isalpha():
    print ("That's not a valid input. Please enter a number!")
    salary3 = input("What is " + str(name3) + "'s weekly income?")
salary3 = float(salary3)

#Get name3's expense information
mortgage3 = input("What is " + str(name3) + "'s weekly mortgage expense?")
while len(mortgage3) < 1 or mortgage3.isalpha():
    print ("That's not a valid input. Please enter a number!")
    mortgage3 = input("What is " + str(name3) + "'s weekly mortgage expense?")
mortgage3 = float(mortgage3)

grocery3 = input("What is " + str(name3) + "'s weekly grocery expense?")
while len(grocery3) < 1 or grocery3.isalpha():
    print ("That's not a valid input. Please enter a number!")
    grocery3 = input("What is " + str(name3) + "'s weekly grocery expense?")
grocery3 = float(grocery3)

power3 = input("What is " + str(name3) + "'s weekly power expense?")
while len(power3) < 1 or power3.isalpha():
    print ("That's not a valid input. Please enter a number!")
    power3 = input("What is " + str(name3) + "'s weekly power expense?")
power3 = float(power3)

vehicle3 = input("What is your weekly vehicle expense?")
while len(vehicle3) < 1 or vehicle3.isalpha():
    print ("That's not a valid input. Please enter a number!")
    vehicle3 = input("What is " + str(name3) + "'s weekly vehicle expense?")
vehicle3 = float(vehicle3)

#Add expenses together for total expenses
weekly_expenses3 =  float(mortgage3 + grocery3 + power3 + vehicle3)
#Subtract expenses from income for left over amount
left_over3 = float(salary3 - weekly_expenses3)
#Give needed savings a value (10%)
needed_savings3 = float(salary3 * .1)

#Format displayed amounts to give 2 decimal places
display_salary3 = format(salary3, ".2f")
display_weekly_expenses3 = format(weekly_expenses3, ".2f")
display_left_over3 = format(left_over3, ".2f")
display_needed_savings3 = format(needed_savings3, ".2f")

#Output name1's information
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

#Decide whether amount left over is at least 10% of salary
if left_over1 < needed_savings1:
    print ("")
    print (name1.strip(), "needs to save more money.")
else:
    print ("\nCongratulations,", name1, end  = '')
    print (", you are on your way to financial freedom!")

#Output name2's information
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

#Decide whether amount left over is at least 10% of salary
if left_over2 < needed_savings2:
    print ("")
    print (name2.strip(), "needs to save more money.")
else:
    print ("\nCongratulations,", name2, end  = '')
    print (", you are on your way to financial freedom!")

#Output name3's information    
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

#Decide whether amount left over is at least 10% of salary
if left_over3 < needed_savings3:
    print ("")
    print (name3.strip(), "needs to save more money.")
else:
    print ("\nCongratulations,", name3, end  = '')
    print (", you are on your way to financial freedom!")


