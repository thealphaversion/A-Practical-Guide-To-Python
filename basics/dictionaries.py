# dictionary is an unordered collection fo data
# it stores data as key-value pairs

# create a dictionary
numbers_and_letters = {1: "A", 2: "B", 3:"C", 4:"D", 5:"E"}

print("Dictionary:", numbers_and_letters)



# access values in a dictionary
# value = dictionary_name[key]
value_of_key_1 = numbers_and_letters[1]

# or you can use the  get() method
value_of_key_3 = numbers_and_letters.get(3)

print("value of key 1:", value_of_key_1)
print("value of key 3:", value_of_key_3)


# get the list of values using the values() method
print("\nAll values:", numbers_and_letters.values())

# get the list of keys using the keys() method
print("All keys:", numbers_and_letters.keys())

# add items to a dictionary
# dictionary_name[key] = values

numbers_and_letters[14] = "My birthday!"

print("\nDict:", numbers_and_letters)

# delete items from a dictinary using the del keyword

del numbers_and_letters[14]

print("\nAfter deletion:", numbers_and_letters)

# or using the pop() method which removes the key-pair value of the specified key
print("After Popping:", numbers_and_letters.pop(2))
print("After using pop:", numbers_and_letters)

# or use popitem() to remove the last inserted value
print("Popitem:", numbers_and_letters.popitem())
print("After using popitem:", numbers_and_letters)

# use clear() to clear the dictionary
numbers_and_letters.clear()
print("After clearing:", numbers_and_letters)


# copy a dictionary using the copy() method
# just doing dictionary2 = dictionary1 does not copy the dictionary
# rather dictionary2 is assigned a reference to dictionary1

dictionary1 = {"One":"First", "Two":"Second", "Three":"Third", "Four":"Fourth"}

dictionary2 = dictionary1.copy()


# loop through a dictionary
print()

for key in dictionary1:
    print(key)

print()
for key, value in dictionary1.items():
    print(key, value) 


# find max value in a dictionary

maximum = max(dictionary1, key=dictionary1.get) 
print("Max value:", maximum, dictionary1[maximum])

# similarly you can use the min function to get the minimum value