


#The general recipe for calling functions and saving the result to a variable is thus:
#output = function_name(input)

#Familiar
# Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: print() and type(). You've also used the functions str(), int(), bool() and float() to switch between data types. These are built-in functions as well.

# Calling a function is easy. To get the type of 3.0 and store the output as a new variable, result, you can use the following:

# result = type(3.0)
# The general recipe for calling functions and saving the result to a variable is thus:

# output = function_name(input)
# Instructions
# 100 XP
# Use print() in combination with type() to print out the type of var1.
# Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
# Use int() to convert var2 to an integer. Store the output as out2.

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
int(var2)
print(var2)

### HELP
# Maybe you already know the name of a Python function, but you still have to figure out how to use it. Ironically, you have to ask for information about a function with another function: help(). In IPython specifically, you can also use ? before the function name.

# To get help on the max() function, for example, you can use one of these calls:

# help(max)
# ?max
# Use the IPython Shell to open up the documentation on pow(). Which of the following statements is true?
help(pow)
### MULTIPLE ARGUMENTS

# In the previous exercise, you identified optional arguments by viewing the documentation with help(). You'll now apply this to change the behavior of the sorted() function.

# Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

# You'll see that sorted() takes three arguments: iterable, key, and reverse.

# key=None means that if you don't specify the key argument, it will be None. reverse=False means that if you don't specify the reverse argument, it will be False, by default.

# In this exercise, you'll only have to specify iterable and reverse, not key. The first input you pass to sorted() will be matched to the iterable argument, but what about the second input? To tell Python you want to specify reverse without changing anything about key, you can use = to assign it a new value:

# sorted(____, reverse=____)
# Two lists have been created for you. Can you paste them together and sort them in descending order?

# Note: For now, we can understand an iterable as being any collection of objects, e.g., a List.

# Instructions
# Use + to merge the contents of first and second into a new list: full.
# Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
# Finish off by printing out full_sorted.

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full


# Sort full in descending order: full_sorted


# Print out full_sorted
