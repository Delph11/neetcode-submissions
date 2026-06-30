# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next: 
        # 1. if we have the fast pointer at the last position but then we checked only if fast id null or not and we found it is not so the lop jumps onece again. NOw the next posn. is null, so pointer jumps once. But then pointer jumps again and this time the pointer is going next to NOne. It is invalid and throw and error saying the None type has no Next attribute. 
        # 2. If we have the pointer at the second last position then the pointer jumps to the null position . NOw we will check the loop if we have the fast.next as none and then the loop will throw an error necause fast is at None and the None don't have a next attribute
        # 3. This is why we need to check for both the fast and the fast.next 
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
