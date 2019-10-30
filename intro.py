#Python3

#Declaring variables

#Python is a dynamically typed language and will assume the type of data that is assigned to a variable
x = 5
y = "Apple"
z = 30.0

a = b = c = "Same value assigned to multiple variables"

one, two, three = 1, 2, 3                       #multiple variables assigned values in the same line


#Printing output

print(x)                                        #will print the value of x along with sending the cursor to a newline

print(y, end='')                                #will print the value of y without sending the cursor to a newline

print("Z:", z)                                  #will print "Z:" and append the value of z after it with a space between them

print("a: " + a)                                #will print "a:" and append the value of a after it

print("b:", b, ", c:", c)                       #will print b and c

print("one:", one, "two:", two)                 #will print one and two

print("one: " + str(one) + " two: " + str(two)) #will print one and two, but we have to typecast interger values to string because the + operator
                                                #can only concatenate string objects and not integer

print(type(x), type(y))                         #prints the data type of the variable that python inferred from the value assigned to it

"""
This is a multi line comment

The following has been taken from w3schools -

Rules for defining variables: 
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""