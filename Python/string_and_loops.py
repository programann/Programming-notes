### RANGES
#Ranges are a very simple type of sequence that is most commonly used in for loops. Ranges can only contain integers in a fixed pattern. You can build a range using the range() constructor method and loop through it as if it were a standard list.

#The range constructor only requires one argument: the end of the range. You may have noticed above that this top value is not included in the range itself. This is similar to how slicing works in lists.
for n in range(4):
    print(n)

# => 0
# => 1
# => 2
# => 3
#There are two optional arguments that you can include when creating a range: a start value and a step size.

# range(4) gives us 0, 1, 2, 3
# range(1, 4) gives us 1, 2, 3
# range(0, 4, 2) gives us 0, 2
for n in range(0,4,2):
    print(n)



### STRINGS
my_string = 'Hello world!'
for char in my_string:
    print(char)

# => H
# => e
# => l
# => l
# => o
# => 
# => w
# => o
# => r
# => l
# => d
# => !


my_string[0]
# => 'H'

#Changing Case
# Strings can be formatted for case using three methods:

# str.upper() returns an uppercase version of the original string.
# str.lower() returns a lowercase version of the original string.
# str.title() returns the original string in titlecase (with the first letter of each new word capitalized.)