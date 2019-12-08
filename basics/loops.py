
# if-else
# if statement one is true, then do something
# if not then do something else
# easy peasy lemon squeezy

left = 200
right = 33

if left > right:
    print("Left is greater than Right")
elif left == right:
    print("Left and Right are equal")
else:
    print("Right is greater than Left")

print()
# and and or
if left > 50 and right > 10:
    print("Yes!")
else:
    print("No!")

if left < 100 or right > 10:
    print("Yes!")
else:
    print("No!")


# for loop
# loop through each value in an iterable
print()
a_list = [1, 4, 6, 8, 9, 7, 8, 5, 8, 4]

for value in a_list:
    print(value)

for i in range(len(a_list)):
    print(i, a_list, i + a_list[i])


# while loop
# as long as the condition is true, repeat the block of code
print()
i = 0
while(i < len(a_list)):
    print(a_list[i], end=' ')
    i = i + 1