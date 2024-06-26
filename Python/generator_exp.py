# Generator expressions are very similar to list comprehensions. They use almost identical syntax to produce iterable objects in a single line:

one_to_three = range(1,4)

# A list comprehension uses square brackets
squared_lc = [n ** 2 for n in one_to_three]

# A generator expression uses parentheses
squared_ge = (n ** 2 for n in one_to_three)

# Looping through each shows identical values...
for n in squared_lc:
    print(n)

# 1
# 4
# 9

for n in squared_ge:
    print(n)

# 1
# 4
# 9

# But the objects are NOT identical
print(squared_lc)
# [1, 4, 9]
print(squared_ge)
# <generator object <genexpr>>


## Generator expressions take up less memory space than list comprehensions.
# sys allows us to look into system memory, among other things
import sys

list_comprehension = [n for n in range(100000)]
generator_expression = (n for n in range(100000))

# Returns the size of an object in bytes
print(sys.getsizeof(list_comprehension))
# 824456
print(sys.getsizeof(generator_expression))
# 112