

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, value):
        self.head = ListNode(value)
        self.tail = self.head
        self.length =1

    def append(self, value):
        node = ListNode(value)
        self.tail.next=node
        self.length+=1
        return self
    
    def prepend(self, value):
        node = ListNode(value)
        node.next=self.head
        self.head =node
        self.length+=1
        return self

    def displayLinkedList(self):
        print('Displaying the list')
        node = self.head
        if node == None:
            print("node is none")
        while(node != None):
            print(node.val)
            node = node.next

    def reverse(self):
        if not self.head.next:
            return self.head

        else:
            first = self.head
            second = first.next
            while(second):
                temp = second.next
                second.next = first
                first = second
                second = temp
            
            self.head.next = None
            self.head = first

        return self.head


myLinkedList = LinkedList(10)

myLinkedList.append(20)
myLinkedList.prepend(45)
myLinkedList.displayLinkedList()
# print(myLinkedList.head.val)
myLinkedList.reverse()
myLinkedList.displayLinkedList()
