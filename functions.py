x = 5
y = "Apple"
z = 30.0

a = b = c = "Same value assigned to multiple variables"

one, two, three = 1, 2, 3

def printX():                                       #This defines a function
  print("X is:", x)                                 #Function body

printX()                                            #Function call

def changeValueOfX(newValue):
    x = newValue
    printX()


if __name__ == "__main__":
    changeValueOfX("new value of x")            

# the value of x did not change. This is because the x referred to by
# the printX function is the globally declared x, i.e. the x at the top, x = 5
# global variables can also be declared by the keyword global


def changeValueofXForReal(newValue):
    global x
    x = newValue
    printX()

changeValueofXForReal("value changed now")