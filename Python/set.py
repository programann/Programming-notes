## Instantiating a set using a sequence is a good way to isolate unique members:

my_list = [1, 2, 1, 3, 2]
print(set(my_list))
# => {1, 2, 3}

#..though it is important to remember that sets are unordered, so our output might not be pretty:

my_string = "the big red cat ate the fat rat"
print(set(my_string))
# => {'g', 'h', 'b', 'r', 'e', 'd', 'f', 'c', 't', 'a', 'i', '

# To determine if two collections have the same members, we can check their sets:

print(set(range(1, 10)) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# => True

# If the sets are not identical, we can use the intersection & operator to see what they have in common:
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
print(set_1 & set_2)
#=> 3

# ...or we can check for differences using the difference - operator:
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
print(set_1 - set_2)
# => {1, 2}
print(set_2 - set_1)
# => {4, 5}

# Using these operators also allows us to dynamically modify sets as our program runs:
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_1 &= set_2
#=> {3}
set_2 -= set_1
# {4, 5}

# Sets also support comprehensions with the same syntax as lists:

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
unique_consonants = {c.lower() for c in sentence if c not in "aeiou ,."}
print(unique_consonants)
# {'g', 'p', 'b', 'l', 'r', 'd', 'm', 'q', 'c', 't', 's', 'n'}