### YOUR FIRST 2D NUMPY ARRAY 

# Before working on the actual MLB data, let's try to create a 2D numpy array from a small list of lists.

# In this exercise, baseball is a list of lists. The main list contains 4 elements. Each of these elements is a list containing the height and the weight of 4 baseball players, in this order. baseball is already coded for you in the script.

# Instructions
# 100 XP
# Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
# Print out the type of np_baseball.
# Print out the shape attribute of np_baseball. Use np_baseball.shape.

# Import numpy
import numpy as np

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

### SUBSETTING 2D NUMPY ARRAYS
# If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

# # regular list of lists
# x = [["a", "b"], ["c", "d"]]
# [x[0][0], x[1][0]]

# # numpy
# import numpy as np
# np_x = np.array(x)
# np_x[:, 0]
# For regular Python lists, this is a real pain. For 2D numpy arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

# The code that converts the pre-loaded baseball list to a 2D numpy array is already in the script. The first column contains the players' height in inches and the second column holds player weight, in pounds. Add some lines to make the correct selections. Remember that in Python, the first element is at index 0! baseball is available as a regular list of lists.

# Instructions

# Print out the 50th row of np_baseball.
# Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
# Select the height (first column) of the 124th baseball player in np_baseball and print it out.

# Import numpy package
import numpy as np

#Create 
height_in = [180, 215, 210, 210, 188, 176, 209, 200]
weight_lb = [180, 215, 210, 210, 188, 176, 209, 200]
for i in range (150):
    weight_lb.append(i)
np_weight_lb = np.array(weight_lb)
for i in range (150):
    height_in.append(i)
np_height_in = np.array(height_in)

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
for i in range(150):
    baseball.append([i, i + 1])
np_baseball = np.array(baseball)
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])

###     2D ARITHMETRIC
# Remember how you calculated the Body Mass Index for all baseball players? numpy was able to perform all calculations element-wise (i.e. element by element). For 2D numpy arrays this isn't any different! You can combine matrices with single numbers, with vectors, and with other matrices.

# Execute the code below in the IPython shell and see if you understand:


# Explain
# import numpy as np
# np_mat = np.array([[1, 2],
#                    [3, 4],
#                    [5, 6]])
# np_mat * 2
# np_mat + np.array([10, 10])
# np_mat + np_mat
# np_baseball is coded for you; it's again a 2D numpy array with 3 columns representing height (in inches), weight (in pounds) and age (in years). baseball is available as a regular list of lists and updated is available as 2D numpy array.

# Instructions
# 100 XP
# You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
# You want to convert the units of height and weight to metric (meters and kilograms, respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
# Multiply np_baseball with conversion and print out the result.


# Import numpy package
import numpy as np

# Create base and update
for i in range (150):
   baseball.append(i)
for i in range (150):
    updated.append(i)
# Create np_baseball ( cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
updated = np_baseball
print(np_baseball + updated)

# Create numpy array: conversion
conversation = np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(np_baseball * conversation)