# ### PARTITION LIST

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 
# https://leetcode.com/problems/partition-list/description/

# tc - O(n), sc - O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = less = ListNode(0)
        head2 = greaterEqual = ListNode(0)

        while head :
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greaterEqual.next = head
                greaterEqual = greaterEqual.next
            head = head.next
        
        greaterEqual.next = None
        less.next = head2.next
        return head1.next
                
        
                    

