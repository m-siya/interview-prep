# ### DOUBLE A NUMBER REPRESENTED AS A LINKED LIST

# You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

# Return the head of the linked list after doubling it.

# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# tc - O(n + 2n), sc - O(n)
class Solution:
    def doubleDigits(self, digits: [int]) :
        num = 0
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            double = 2 * digits[i] + carry
            digits[i] = double % 10
            carry = double // 10
        
        if carry: digits.insert(0, carry)

        return digits


    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        digits = []

        curr = head

        while curr:
            digits.append(curr.val)
            curr = curr.next
        
        double = self.doubleDigits(digits)


        num_index = 0
        curr = head

        while curr.next:
            curr.val = int(double[num_index])
            num_index += 1
            curr = curr.next

        
        curr.val = int(double[num_index])


        if num_index < len(double) - 1:
            num_index += 1
            curr.next = ListNode(int(double[num_index]))
        
        

        return head
