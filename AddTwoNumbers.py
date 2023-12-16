# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = l3 = ListNode()
        parent = None
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1 = ListNode()
            if l2 is None:
                l2 = ListNode()

            res = l1.val + l2.val + l3.val
            l3.val = res % 10

            # l3.next must always be set otherwise we will loose reference
            if res >= 10:
                l3.next = ListNode(1)
            else:
                parent = l3
                l3.next = ListNode()

            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        if l3.val == 0:
            parent.next = None
        return head
