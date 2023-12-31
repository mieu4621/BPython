### Your First NumPy Array
# In this chapter, we're going to dive into the world of baseball. Along the way, you'll get comfortable with the basics of numpy, a powerful package to do data science.

# A list baseball has already been defined in the Python script, representing the height of some baseball players in centimeters. Can you add some code here and there to create a numpy array from it?

# Instructions

# Import the numpy package as np, so that you can refer to numpy with np.
# Use np.array() to create a numpy array from baseball. Name this array np_baseball.
# Print out the type of np_baseball to check that you got it right.

# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

### BASEBALL PLAYERS' HEIGHT 
# You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask around for some more statistics on the height of the main players. They pass along data on more than a thousand players, which is stored as a regular Python list: height_in. The height is expressed in inches. Can you make a numpy array out of it and convert the units to meters?

# height_in is already available and the numpy package is loaded, so you can start straight away (Source: stat.ucla.edu).

# Instructions
# 100 XP
# Create a numpy array from height_in. Name this new array np_height_in.
# Print np_height_in.
# Multiply np_height_in with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
# Print out np_height_m and check if the output makes sense.

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
height_in = [180, 215, 210, 210, 188, 176, 209, 200]
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200]
for i in range (120):
    weight_lb.append(i)
for i in range (120):
    height_in.append(i)
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

# BASEBALL PLAYER'S BMI
# The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height_in and weight_lb. height_in is in inches and weight_lb is in pounds.

# It's now possible to calculate the BMI of each baseball player. Python code to convert height_in to a numpy array with the correct units is already available in the workspace. Follow the instructions step by step and finish the game! height_in and weight_lb are available as regular lists.

# Instructions
# 100 XP
# Create a numpy array from the weight_lb list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting numpy array as np_weight_kg.
# Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation:
 
# Save the resulting numpy array as bmi.
# Print out bmi.

# Import numpy
import numpy as np

# Create array from height_in with metric units: np_height_m
np_height_m = np.array(height_in) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / (np_height_m ** 2)

# Print out bmi
print(bmi)

### LIGHTWEIGHT BASEBALL PLAYERS 
# To subset both regular Python lists and numpy arrays, you can use square brackets:

x = [4 , 9 , 6, 3, 1]
# x[1]
import numpy as np
y = np.array(x)
# y[1]
# For numpy specifically, you can also use boolean numpy arrays:

high = y > 5
print(high)
print(y[[0,1,3,4,0]])
print(y[[False,True,True,False,False]])
# The code that calculates the BMI of all baseball players is already included. Follow the instructions and reveal interesting things from the data! height_in and weight_lb are available as regular lists.

# Instructions
# 100 XP
# Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
# Print the array light.
# Print out a numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])

### SUBSETTING NUMPY ARRAYS

# You've seen it with your own eyes: Python lists and numpy arrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:

# x = ["a", "b", "c"]
# x[1]

# np_x = np.array(x)
# np_x[1]
# The script in the editor already contains code that imports numpy as np, and stores both the height and weight of the MLB players as numpy arrays. height_in and weight_lb are available as regular lists.

# Instructions
# 100 XP
# Subset np_weight_lb by printing out the element at index 50.
# Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.
# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])