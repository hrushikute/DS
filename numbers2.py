# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    def summation(self,num1, num2):
        return num1+num2
    
    def convert_to_number(self, list_val):
        '''
        :type list_val: ListNode
        :rtype : int
        
        '''
        number_of_zeros = 1
        num = 0
        while(list_val != None):
            num = num + (list_val.val*number_of_zeros)
            number_of_zeros = number_of_zeros * 10
        
        return num
    
    def convert_to_list(self, num):
        '''
        :type : num : int
        :rtype list_val: ListNode
        '''
        number_of_zeros = 10
        quotient = num/number_of_zeros
        while(quotient >=1):
            if number_of_zeros ==10:
                head = ListNode
                head.val = quotient
                tail = head
            else:
                newNode=ListNode
                newNode.val=quotient
                tail.next = newNode
                tail = newNode
            
            number_of_zeros = number_of_zeros * 10
            quotient = num/number_of_zeros
            
        return head  
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = self.convert_to_number(l1)
        num_2 = self.convert_to_number(l2)
        
        sum_val = self.summation(num1,num2)
        
        output_list = self.convert_to_list(sum_val)
        
        return output_list
    
     
    def append(self, value):
        node = ListNode(value)
        self.tail.next=node
        self.length+=1
        return self      
            
    