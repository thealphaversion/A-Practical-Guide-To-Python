# I was going to do numbers and strings together but nope, we ain't doing it that way

# write a string using " " or ' '

"this is a string"
'this is also a string'

""" this
is
also
a
string
"""

'''
this
as
well
'''

"i'll stop being annoying now"

a_string_variable = "assign a string to a variable"

print("i know this seems stupid but yeah, this is how you print strings")

# okay enough playing around

example_string = "hello world"

# access elements of a string using []
# string indexes start from 0

x = example_string[4]
print(x)
print(example_string[6])
print(example_string[-2])               #access elements from the right

# get a range of elements

y = example_string[3:7]
print(y)
print(example_string[-2:-5])

# some string methods now

another_example = "   Hello world  "

uppercase = another_example.upper()

lowercase = another_example.lower()

length_of_string = len(another_example)

remove_white_spaces = another_example.strip()

split_space_seperated_string_into_list = another_example.split(" ")

a_string = "Hi, Hello"
split_string_into_list_by_comma = a_string.split(",")

print("orignal string:", another_example)
print("uppercase: ", uppercase)
print("lowercase: ", lowercase)
print("remove white spaces: ", remove_white_spaces)
print("split with space: ", uppercase)

print("\nother example string:", a_string)
print("split string with comma:", split_string_into_list_by_comma)

# you can use different operators to split the string with

# there are lots of string methods, i'll keep on adding more in the future,
# but till then please check out the python documentation for more methods

# concat string

string_one = "first string"
string_two = " second string"

concat_string = string_one + string_two

print("\nstring one: ", string_one)
print("string two: ", string_two)
print("concat string: ", concat_string)

# concat string and numbers using the format method

an_integer_num = 775
a_floating_num = 44.5

string_for_formatting = "\nThe integer number is {} and the floating number is {}."

print(string_for_formatting.format(an_integer_num, a_floating_num))

# find substrings in string

print("find:", string_for_formatting.find("he"))                 # this will return the first index where it found the substring

print("rfind:", string_for_formatting.rfind("he"))               # this will return the last index where it found the substring