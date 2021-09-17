

class Node(object):
    def __init__(self,value=0,next=None): 
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length =0

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.length +=1
    
    def pop(self):
        if (self.top != None):
            poped_value = self.top.value
            self.top=self.top.next
            print(f'Poped value: {poped_value} ')
        else:
            print("Stack is Empty")

    def peek(self):
        print(self.top.value)

    def printStack(self):
        pointer = self.top
        stackList = []
        while(pointer != None):
            stackList.append(pointer.value)
            pointer = pointer.next
        
        print(f"Stack : {stackList}")

myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)
myStack.printStack()
myStack.pop()
myStack.printStack()
myStack.peek()