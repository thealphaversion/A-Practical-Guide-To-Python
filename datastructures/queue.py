# a queue is a data structure in which the data element entered first is removed first
# basically you insert elements from one end and remove them from another end

# a very simple, and cliche example would be that of a plain old queue at McDonald's
# The person who joined the queue first will order first, and the one who joined last will order last
# (unless you're a prick)

# queues have two important operations:
# queue
# dequeue

# queuing is basically entereing a new element to the end of the queue
# dequeing is removing an element from the front of the queue

# let us try to build a queue using an array

# we will have a few functions
# one to queue new elements
# one to dequeue elements
# one to print the queue
# one to get the front of the queue
# one to get the end of the queue
# one to check if the queue is empty

class OurQueue:
    def __init__(self):
        self.front = -1
        self.end = -1
        self.elements = []
    
    def queue(self, value):
        self.front = self.front + 1
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