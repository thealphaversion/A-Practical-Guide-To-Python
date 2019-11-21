# a list is an important data type in python
# lists are ordered and mutable i.e. they are built in order and can be changed

list_example = [3, 5, 22]

mixed_list = [44, "a string", 96, 33, "value"]              # lists can have different types of data as items

print(list_example)
print(mixed_list)

# to access a particular element in a list
# list indexes start from 0

value_at_index_1 = mixed_list[1]                
value_at_index_4 = mixed_list[4]

value_at_3rd_index_from_right = mixed_list[-3]              # indexes from right start at -1

print("1: ", value_at_index_1)
print("4: ", value_at_index_4)
print("-3: ", value_at_3rd_index_from_right)

# range of indexes

long_list = [3, 55, 33, 24, 54, 87, 54, 22, 77, 87, 2]      # lists can have duplicate values

sublist = long_list[3: 7]

print("\nlonglist:", long_list)
print("sublist:", sublist)

# change value at an index

long_list[0] = 999
print("\nlonglist after change in value:", long_list)

# add new value to list

# here we add the value 1 to the end of the list
long_list.append(1)                                                 # adds new value to the end of the list

# here we add the value 55 after the element at the 0th index
long_list.insert(0, 55)                                             # adds new value after the specified index
