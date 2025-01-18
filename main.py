# Write a program that takes input from user and determine if the given number is odd or even?
#number = int(input ("Enter number"))

#if number%2==0:
    #print("This number is even")
#else:
    #print("This number is odd") 


# A company decided to give a bonus of 7% to employees if his/her year of service is more than 3 years
# Ask user for their salary and year of service and print the net bonus amount

#pseudocode
# Start 
# Input - What is your salary?
# Input - What year did you start this employement?
# Calculate the difference in years between now and when they started
# If years of service > 3, they recieve a 7% bonus on their salary
# Else they do not recieve any bonus
# End

# *Always define the data type
# Concantation must be , when combining different data types NOT +

salary = float (input ("What is your current salary?"))
service = int (input ("What year did you start this employement?"))
if 2025-service>3:
    print ("Net bonus =" , (salary*0.07)) 
else:
    print("Unfortunately, you are not eligible for a bonus")




