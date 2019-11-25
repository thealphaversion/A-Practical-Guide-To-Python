# sets have elements that are unordered, unindexed and unique

fruit_set = {"apple", "banana", "cherry"}
print("Fruit Set:", fruit_set)

# sets only contain unique elements

random_set = {3, 4, 6, 6}
print("\nRandom set:", random_set)                  # it will only print unique elements

# add elements to a set by using the add() method

random_set.add(77)
print("\nRandom set:", random_set)

# to add multiple elements use the update() method
random_set.update([23, 43, 66])

# or

a_list = [26, 34, 38, 83]
random_set.update(a_list)
 
print("\nRandom set after add and update:", random_set)

# the update method updates the set by taking a union of the iterable with itself


# remove elements from a set using the remove() or discard() methods

random_set.remove(26)
random_set.discard(83)

print("\nRandom set after remove and discard:", random_set)

# if the element to be removed does not exist then
# remove() raises and error
# discard() does not raise an error

# delete the element using the clear() method or the del keyword

random_set.clear()                                       # comment this line to try the del keyword below

# or

# del random_set                                         # remove the comment to try