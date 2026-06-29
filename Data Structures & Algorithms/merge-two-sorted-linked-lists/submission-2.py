# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = list1
        j= list2

        head = None
        tail = None

        while (i is not None) or (j is not None):

            if (i is not None) and (j is not None):
                if i.val<=j.val:
                    a = ListNode(i.val)
                    i = i.next
                else:
                    a = ListNode(j.val)
                    j = j.next
            
            elif (i is not None) and (j is None):
                    a = ListNode(i.val)
                    i = i.next
            
            elif (i is None) and (j is not None):
                    a = ListNode(j.val)
                    j = j.next

            

            if head is None:
                head = a
            else:
                tail.next = a
            
            tail = a



        return head