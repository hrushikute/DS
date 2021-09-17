from typing import Counter


class Node(object):
    def __init__(self, value=0, next=None):
        self.value=value
        self.next=next

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length=0

    def peek(self):
        print(self.first)
        return

    def enqueue(self,value): 
        newNode = Node(value)
        if self.first == None:
            self.last = newNode
            self.first = self.last
            self.length+=1
        else:
            self.last.next = newNode
            self.last=newNode
            self.length+=1

    def dequeue(self):
        if self.first == None:
            print("Queue is empty")
        else:
            print(f"DeQueued Element : {self.first.value}")
            self.first = self.first.next
            self.length -=1
    
    def printQueue(self):
        print(self.length)
        # second = self.first.next
        # third = second.next
        # print(f'{self.first.value}->{second.value} ->{third.value}')
        if self.first == None and self.last == None:
            print("Queue is empty")
        else:
            pointer=self.first
            # counter = 1
            while (pointer != None):
                # print(counter)
                print(pointer.value)
                pointer=pointer.next
                # counter +=1


myQueue = Queue()
myQueue.enqueue("Notepad")
myQueue.enqueue("Outlook")
myQueue.enqueue("Pycharm")
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()

