

class Node:
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:            
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    # print method for the linked list
    def __str__(self):
        my_str = ''
        current = self.head
        while current:
            my_str += str(current.data)
            current = current.next
        return my_str

# Singly Linked List with insertion and print methods
def add_integers(integer1, integer2) -> LinkedList():
    result = LinkedList()
    # last = None
    carry = 0
    while (integer1 != None or integer2 != None or carry > 0): 
        first = (0 if integer1 == None else integer1.data)
        second = (0 if integer2 == None else integer2.data)
        
        sum = first + second + carry
        result.insert(sum % 10)
        carry = sum // 10 # take the 10's digit from the integer division

        if integer1 != None:
            integer1 = integer1.next

        if integer2 != None:
            integer2 = integer2.next
    
    return result;

# first = LinkedList()
# first.insert(1)
# first.insert(2)
# first.insert(3)
# # first.printLL()

# second = LinkedList()
# second.insert(1)
# second.insert(2)
# # second.printLL()
# # first = create_linked_list([1, 2, 3]) #321
# # second = create_linked_list([1, 2]) #21
# result = add_integers(first.head, second.head)
# print("Sum:", str(result))



def reverse_words(sentence):    # sentence here is an array of characters
    a = sentence.split(' ')
    result = ''
    for i in range(len(a)-1, -1, -1):
        result += a[i] + ' '
    return result

x = reverse_words("hello cruel world")
print( x )