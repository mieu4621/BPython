


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
out2 = int(var2)
print(out2)

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
full = first + second

# Sort full in descending order: full_sorted

full_sorted = sorted(full, reverse=True)
# Print out full_sorted
print(full_sorted)

### STRING METHOD

# Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type help(str) in the IPython Shell.

# A string place has already been created for you to experiment with.

# Instructions

# Use the upper() method on place and store the result in place_up. Use the syntax for calling methods that you learned in the previous video.
# Print out place and place_up. Did both change?
# Print out the number of o's on the variable place by calling count() on place and passing the letter 'o' as an input to the method. We're talking about the variable place, not the word "place"!

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

### LIST METHODS

# List Methods (2)
# Most list methods will change the list they're called on. Examples are:

# append(), that adds an element to the list it is called on,
# remove(), that removes the first element of a list that matches the input, and
# reverse(), that reverses the order of the elements in the list it is called on.
# You'll be working on the list with the area of different parts of the house: areas.

# Instructions
# 100 XP
# Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
# Print out areas
# Use the reverse() method to reverse the order of the elements in areas.
# Print out areas once more.

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)
# you can usse extend() to add elements into list
# areas.extend([24.5,15.45])
# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

### IMPORT PACKET

# As a data scientist, some notions of geometry never hurt. Let's refresh some of the basics.

# For a fancy clustering algorithm, you want to find the circumference, 
# , and area, 
# , of a circle. When the radius of the circle is r, you can calculate 
#  and 
#  as:


# In Python, the symbol for exponentiation is **. This operator raises the number to its left to the power of the number to its right. For example 3**4 is 3 to the power of 4 and will give 81.

# To use the constant pi, you'll need the math package. A variable r is already coded in the script. Fill in the code to calculate C and A and see how the print() functions create some nice printouts.

# Instructions

# Import the math package. Now you can access the constant pi with math.pi.
# Calculate the circumference of the circle and store it in C.
# Calculate the area of the circle and store it in A.

# Import the math package
import math 

# Definition of radius
r = 0.43

# Calculate C

C = 2*(math.pi)*r

# Calculate A
A = r**2 * math.pi

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

### SELECTIVE IMPORT

# General imports, like import math, make all functionality from the math package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:

# from math import pi
# Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius r (in km) that is defined in the script.

# Instructions

# Perform a selective import from the math package where you only import the radians function.
# Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r * phi, where r is the radius and phi is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
# Print out dist.

# Import radians function of math package
from math import radians
from math import pi
# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r *(radians(12))

# Print out dist
print(dist)
