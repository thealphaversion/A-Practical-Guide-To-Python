# Here we'll find the middle element of a singly linked list in one pass
# which is essentially going through the linked list of unknown length once
# and finding the length and the middle element at once

# doing this in one pass instead of the usual two pass stuff will reduce the time required to find the middle element
# but we'll end up using more space
# there is this time-space tradeoff, but life isn't fair so let's get to it

class LinkedListNode:
    def __init__(self, node_value):
        self.value = node_value
        self.next = None
    
def find_middle_element(node):
    end_pointer = node
    middle_pointer = node

    while(node.next is not None):
        end_pointer = end_pointer.next
        node = node.next
        end_pointer = end_pointer.next
        middle_pointer = middle_pointer.next
        node = node.next
    
    return middle_pointer

if __name__ == '__main__':
    root = LinkedListNode(44)
    root.next = LinkedListNode(12)
    root.next.next = LinkedListNode(23)
    root.next.next.next = LinkedListNode(40)
    root.next.next.next.next = LinkedListNode(77)

    middle = find_middle_element(root)

    print("The middle element is:", middle.value)