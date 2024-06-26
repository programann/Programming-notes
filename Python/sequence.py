s = [4, 6, 3, 9, 3, 5, 1, 2]
# This will show the truthiness of the number 1 in s
print(1 in s)

#This will add the same copy of the contents of s and stack them
print (s+s)

# Is the same as  s+s
print(s*2)

# Shows the value at the index stated i.e) at one which is 6
print(s[1])

# Shows the number of number from index 3 to 5 
print(s[2:5])


# Returns the number of items in the list
print(len(s))

# shows the minimum in the list
print(min(s)) #max() wil do the opposite

# Rturns the index at which an item is in an array
print(s.index(4))# 4 is at index 0

#shows the number of times a single value is repeated in a single list
print(s.count(9))


### Sorting Lists

s.sort()
print(s)##Also works with strings by using alphabetical order

## We can also use a key parameter to specify with which way we want the sorting to be done

my_list = ['This is a long sentence', 'Word', 'z']

# What if we want to sort by the length of the string?
# We can use the key attribute to tell the sort function to sort using the len function.

my_list.sort(key = len)
print(my_list)
# => ['z', 'Word', 'This is a long sentence']

# If we want to sort in descending order we can pass in the reverse parameter into sort.
my_list = ['This is a long sentence', 'Word', 'z']
my_list.sort(key = len, reverse=True)
print(my_list)
# => ['This is a long sentence', 'Word', 'z']

# The sorted() function returns a sorted copy of the original list
#This function should be used when you want to preserve the integrity of your original list, but you need a sorted version for a separate task.

my_list = [3, 6, 4, 2, 1, 5]
sorted_list = sorted(my_list)
print(my_list)
# => [3, 6, 4, 2, 1, 5]
print(sorted_list)
# => [1, 2, 3, 4, 5, 6]
#We can still pass a key and reverse parameters into sorted() like for the sort() method

     ### ADDING TO LISTS

# We can modify a list like so:
# Remember the s list
s[0] = None
print(s)

# There are two ways of adding to a list:
#The append() and insert()
# Using append
my_list = [0, 1, 2, 3]
my_list.append(4)
print(my_list)
# => [0, 1, 2, 3, 4]

##Using insert
my_list = ['a', 'b', 'c', 'd', 'f']
my_list.insert(4, 'e')
print(my_list)
# => ['a', 'b', 'c', 'd', 'e', 'f']
my_list.insert(1000, 'g')
print(my_list)
# => ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    #### REMOVING FROM LISTS
# 1.The del()
#del() removes elements from a list, specified by an index or range of indices.
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del(my_list[0])
print(my_list)
# => ['b', 'c', 'd', 'e', 'f', 'g']
del(my_list[0:3])# See here it does 3-1
print(my_list)
# => ['e', 'f', 'g']

#2.The pop()
#list.pop() removes and returns the element at the index passed in as an argument. When used without any arguments, it removes and returns the last element of the list.
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
popped_list = my_list.pop()
print(popped_list)
# => 'g'

#3.remove()
#list.remove() removes the element passed in as an argument. This is one of the few list methods that searches by value instead of index!
my_list.remove('f')
print(my_list)
# => ['b', 'c', 'd', 'e']

# 3.The clear()
# list.clear() erases all of the values of a list. This is usually not a very useful tool, but it's a fast way to free up memory on your device if you're working with a particularly large list in the Python shell.
my_list.clear()
print(my_list)
# => []