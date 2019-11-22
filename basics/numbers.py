# numbers can be int, float or complex

# integer example
x = 1
number = 132

# float example
y = 77.5
floating_number = 4.0

# complex example
z = 3j
complex_num = 40 + 2j

# all numeric types can be converted to one another
# except in the case of complex numbers
# complex numbers cannot be converted to int or float

int_to_float_x = float(x)
int_to_complex_x = complex(x)

float_to_int_y = int(y)
float_to_complex_y = complex(y)

# remove the following comment to try it out
# complex_to_int_z = int(z)             #this line will give you an error

print("x:", x)
print("int_to_float_x:", int_to_float_x)
print("int_to_complex_x:", int_to_complex_x)
print("\ny:", y)
print("float_to_int_y:", float_to_int_y)
print("float_to_complex_y:", float_to_complex_y)

# we reqire random numbers, so might as well look at it

import random
print("\nrandom number:", random.randrange(100,999))