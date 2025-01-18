# 18/01/2025
# Loops
# For loop - printing number from 1 to 10
# syntax below
# for condition:
#    statement...

#for i in range(1,11):
#    print(i)
    # when ever the range is between 1 and 11, print i
    # i - a variable, range - a function

# i=1
# while i < 50:
#    print (i)
#    i = i+1 # incrementing the value of i by 1 // also the same as i +=1


# for loop is used when you know how many times the loop is going to run
# while loop is used when you DON'T  know how many times the loop is going to run

# Write a program in Python that can calculate a given number factorial
# choosing a for loop cause we know how many times we want the loop to run
# factorial of 5 -> 5 * 4 * 3 * 2 * 1 = 120

# number = 1
# for i in range(1,6):
#     number*=i # simpler way -> number = number * i
# print(number)

# The code below will target each character in the string
#  = "Muahmmad"
# for character in myFirstName:
#     print(character)

# The code below will target each number in the list - same as above - just using a different data type
# myList = [1,2,3,4,5,6,7,8,9,10]
# for number in myList:
#     print(number)

# break  - used to break the loop
# continue - to skip the current iteration and move to the next iteration
# pass - to do nothing

i = 2 
if i < 10:
    pass

# loop that runs from 1 to 50
# for i in range(1,51):
#     print(i)
#    if i ==20:
#        break


# The  code below will skip 5 and continue from 6
# for i in range (1,10):
#    if i == 5:
#       continue
#    print (i)
    
# Create a list of 4 favourite countries to visit
# Use a for loop to show each country in the list
# If the 3rd country in the list is spain - print "Yaaay Spain is 3rd in your list of favourite countries"
# If it isn't print "Boo, I can't believe Spain isn't your favourite country!"

# countries = ["France", "Spain", "Germany", "Ireland"]
# for place in countries:
#     print(place)

# if countries[2] == "Spain":
#     print("Yaaay Spain is 3rd in your list of favourite countries")
# else:
#     print("Boo, I can't believe Spain isn't your favourite country!")

# TASK - reverse a string using for loop
# 1. Take the string
# 2. Reverse the string
# 3. Apply the loop 
# 4. Print characters of the reversed string

name = "Hiba" #1. 
reversed = name[::-1] #2.
for character in reversed: #3. 
    print(character) #4. 

for character in name[::-1]: # more simplified - same result
    print(character)


