# a stack is a data structure in which the data element entered last is removed first
# basically you insert elements from one end and also remove them from the same end

# for example, you have a box of pringles and you open it.
# Then you can only take the chips first that were entered last

# stacks have two important operations:
# push
# pop

# pushing is basically entereing a new element in a stack, on the top
# popping is removing an element from the top of the stack

# let us try to build a stack using an array

# we will have 3 functions, one to push new elements
# one to pop elements and one to print the stack

class OurVeryOwnStack:
    def __init__(self):
        self.top = -1
        self.elements = []
    
    def push(self, value):
        self.top = self.top + 1
        self.elements.insert(self.top, value)
    
    def pop(self):
        self.top = self.top - 1
    
    def display(self):
        if(self.top == -1):
            print("Stack is empty!")
        else:
            for i in range(self.top, -1, -1):
                print(self.elements[i], end=' ')


if __name__ == '__main__':
    first_stack = OurVeryOwnStack()
    first_stack.push(1)
    first_stack.push(33)
    first_stack.push(54)

    print("Printing Stack:", end=' ')
    first_stack.display()

    first_stack.pop()
    print("\nAfter popping once:", end=' ')

    first_stack.display()


# stacks also have other methods like peek(), isEmpty() and length()

# lets create a stack with these functions

class OurGreatStack:
    def __init__(self):
        self.top = -1
        self.elements = []
    
    def push(self, value):
        self.top = self.top + 1
        self.elements.insert(self.top, value)
    
    def pop(self):
        if (self.top >= 0):
            self.top = self.top - 1
        else:
            print("Cannot pop because the stack is empty.")

    def peek(self):
        print(self.elements[self.top])
    
    def isEmpty(self):
        if(self.top == -1):
            return True
        else:
            return False
    
    def length(self):
        return self.top + 1
    
    def display(self):
        if(self.top == -1):
            print("Stack is empty!")
        else:
            for i in range(self.top, -1, -1):
                print(self.elements[i], end=' ')

# also try out stack with linked lists, and when you do please contrivute to this project right here lol