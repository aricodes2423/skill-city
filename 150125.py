# 150125
# Collections
# Types of data collections

## 1.  LISTS

# []
# fruit = ["apple","banana","cherry"]
# print(fruit)
# lists are ordered, changeable (can be changed during execution), duplicates (can have duplicates within the list), indexed (assigned a point in the list)- this is a list of strings
# allows you to add as many variables as you want
# index - always starts from 0 
# index = length - 1

# e.g. banana is index number 1
# find out data at index point 4 e.g. print(fruit[3]) - would print mango
# find out the length of the list e.g. print(len(fruit)) - would print 4
# methods - append (adding to a list) , remove (removing from a list, not from a specific index), pop (removing element at a specific index), insert(adding element at a specific index), extend (merge two lists)
#print("Before addition", fruit)
#fruit.append("banana")
#print("After addition", fruit)
#fruit.remove("banana")
#print("After removal", fruit)

# list vs string - ["list"] vs "string"


# complex lists - lists with different types of data e.g. string, integer, boolean etc
# complex list example - fruit = [1, "apple", true]

# method vs function
# attaching a fucntion to a property makes it a method
# e.g. - fruit.pop ... - pop is a method
# e.g. - pop() - pop is a function

# fruit.pop(len(fruit)-1) - 

## 2. TUPLES

# ()
# ordered, UNchangeable (cannot be changed during excecution of the programme), duplicates
# fruit = ("apple","banana","cherry")
# + storing data that you don't want changed
# type casting

## 3. SETS 

# {}
# fruit = {"apple", "banana", "cherry", "cherry"} - will not print two "cherry", will show up in different orders when printed
# unordered, unindexed, no duplicates, unchangeable
# real life example - games for random selections / different combinations - e.g. casino 

## 4. DICTIONARIES


# changeable, ordered, no duplicates
# Phone dictionary - Key Value Pair
# key within brackets - values aftere colon
# phoneDictionary = {
# "John": 1234
# "Jane": 7588
# "Jim": 9940
# }

# sub-dictionaries? - go through...