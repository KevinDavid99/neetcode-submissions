# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle node first
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        current = slow.next
        slow.next = None
        previous = None

        while current:
            temporary = current.next
            current.next = previous
            previous = current
            current = temporary
        # back is the start of the other half list
        back = previous
        front = head

        # the swap reversing
        while back:
            front_temp = front.next
            back_temp = back.next
            front.next = back
            back.next = front_temp
            front = front_temp
            back = back_temp
        return


    
        