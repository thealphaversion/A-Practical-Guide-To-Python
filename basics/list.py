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




# get the length of the list

length_of_list = len(long_list)
print("Length of List:", length_of_list)




# delete elements from a list
print("\nBefore removal:", long_list)
long_list.remove(999)                                                # this will remove the element 55 from the list
print("After removal:", long_list)

# or top remove the last element use the method pop()
long_list.pop()
print("After popping:", long_list)

# another way is to use the del keyword and the index of the element you want to delete
del long_list[0]
print("After deleting:", long_list)

# to delete the entire list, just don't specify the index
del long_list

# or use the clear() method
# long_list.clear()

# print("List", long_list)                              # this line will give you an error
                                                        # remove the comment to try



# sometimes we want to make copies of lists
# we do that using the method copy() and not the operator =
# because the = operator only provides a reference to the orignal list

orignal_list = [1, 5, 7, 15, 33, 46]

copied_list = orignal_list.copy()

reference_to_orignal_list = orignal_list

# changes we do to the copied_list will not affect the orignal list
# but changes to the reference_to_orignal_list will affect the orignal list

print("\n-----------------------------------------------------------------------")

print("Before any operation is done")
print("Orignal List:", orignal_list)
print("Copied List:", copied_list)
print("Reference to the orignal list:", reference_to_orignal_list)

# some insert, delete and manupulation operations

copied_list[0] = 100

reference_to_orignal_list[0] = 0

print("\nAfter operations")
print("Orignal List:", orignal_list)
print("Copied List:", copied_list)
print("Reference to the orignal list:", reference_to_orignal_list)

print("-----------------------------------------------------------------------")


# to combine two lists, use the + operator, or the extend() method
# you can combine any type of data together

first_list = [1, 3, 5, 7, 9]
second_list = [2, 4, 6, 8]

combined_list = first_list + second_list

print("\nFirst list:", first_list)
print("Second list:", second_list)
print("Combined list:", combined_list)

# the extend() method appends another list to one list

print("\nFirst list:", first_list)
print("Second list:", second_list)

first_list.extend(second_list)

print("\nFirst list:", first_list)

# alternatively, you can loop through the lists and append elements indivisually to them

list1 = ['a', 'b', 'c']
list2 = [2, 5, 7]

print("list 1:", list1)
print("list 2:", list2)

for element in list2:
    list1.append(element)

print("list 1 after appending:", list1)