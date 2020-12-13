# Definition for singly-linked list.

# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        out = ListNode(val=0)
        cat = out
        
        while l1 != None or l2 != None:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            
            add = x + y + carry
            carry = add // 10 ## tens place
            base = add % 10 ## ones

            cat.next = ListNode(val=base)
            cat = cat.next
            
            # print(base, carry)
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            cat.next = ListNode(val=carry)
        return out.next

    


l1 = ListNode(val=2)
l1.next = ListNode(val=4)
l1.next.next = ListNode(val=3)

l2 = ListNode(val=5)
l2.next = ListNode(val=6)
l2.next.next = ListNode(val=4)



s = Solution()
out1 = s.addTwoNumbers(l1, l2)

print(out1.val)

while out1.next != None:
    print(out1.next.val)
    out1 = out1.next


'''

Second solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        n1 = 0
        n2 = 0
        i = 1
        
        while l1 != None and l2 != None:
            i1 = l1.val * i
            i2 = l2.val * i
            
            print(i1, i2, l1.val, l2.val)
            
            
            n1 = n1 + i1
            n2 = n2 + i2
            
            
            i = i * 10
            
            if l1.next is not None:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next is not None:
                l2 = l2.next
            else:
                l2.val = 0
        ## number 807
        num = n1 + n2
        print(num, n1, n2)
        
        out = ListNode()
        for i in reversed(str(num)):
            if out.next is None:
                out.val = i
                cat = out
                continue

            new = ListNode(val=i)
            while cat.next is not None:
                cat = cat.next
            cat.next = new
        
        return out
        
        


'''
        