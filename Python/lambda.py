# Instead of using the def keyword to write a function  with the def keyword.

 # Instead of...
#def add_number(x):
    #return x + 1

# we could use lambda and ...
add_number = lambda n: n + 1

# Imagine we wanted to create a function that would add any specific number when invoked. We could write lambdas for each new number, or we could treat our lambda as a first class object and manipulate it inside of another function:

def myfunc(x):
    return lambda n : n + x

new_century = myfunc(100)
print(new_century(2000))

# Lambdas are typically used as arguments and return values. Certain built-in functions, like sorted(), take a function key as an argument to determine which values to sort by:
l = [['red','truck'],['blue','truck'],['red','sedan']]
sorted(l, key=lambda v: v[1])
# => [['red', 'sedan'], ['red', 'truck'], ['blue', 'truck']]
sorted(l, key=lambda v: v[1], reverse=True)
# => [['red', 'truck'], ['blue', 'truck'], ['red', 'sedan']]


#This sorts our list of lists by the values at index 1 (the type of vehicle), with the added option to sort in ascending or descending (reverse=True) order.

# We can also return lambdas as new, unique functions, as seen in the previous section:

def myfunc(x):
    return lambda a,b:(a*b) + x
number = myfunc(100)
print(number(10,10))
# => 200