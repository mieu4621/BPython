# Create a list
# As opposed to int, bool etc., a list is a compound data type; you can group values together:

# a = "is"
# b = "nice"
# my_list = ["my", "list", a, b]
# After measuring the height of your family, you decide to collect some information on the house you're living in. The areas of the different parts of your house are stored in separate variables for now, as shown in the script.

# Instructions
# 100 XP
# Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
# Print areas with the print() function.

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas

print(areas)

# Create list with different types
# A list can contain any Python type. Although it's not really common, a list can also contain a mix of Python types including strings, floats, booleans, etc.

# The printout of the previous exercise wasn't really satisfying. It's just a list of numbers representing the areas, but you can't tell which area corresponds to which part of your house.

# The code in the editor is the start of a solution. For some of the areas, the name of the corresponding room is already placed in front. Pay attention here! "bathroom" is a string, while bath is a variable that represents the float 9.50 you specified earlier.

# Instructions

# Finish the code that creates the areas list. Build the list so that the list first contains the name of each room as a string and then its area. In other words, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
# Print areas again; is the printout more informative this time?

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway",hall,"kitchen",kit,"living room",liv,"bedroom",bed,"bathroom",bath]

# Print areas
print(areas)
    
# Select the valid list
# A list can contain any Python type. But a list itself is also a Python type. That means that a list can also contain a list! Python is getting funkier by the minute, but fear not, just remember the list syntax:

# my_list = [el1, el2, el3]
# Can you tell which ones of the following lines of Python code are valid ways to build a list?

# A. [1, 3, 4, 2] B. [[1, 2, 3], [4, 5, 7]] C. [1 + 2, "a" * 5, 3]

c = [1 + 2, "a" * 5, 3] 
print(type(c))

a = [1, 3, 4, 2]
print(type(a))
b = [[1, 2, 3], [4, 5, 7]]
print(type(b))
# A,B and C are correct anwers