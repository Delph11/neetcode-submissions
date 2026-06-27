# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: # This part takes care of value of the head being none. 
            return None
        if head.next is None: # This part is for LLs with only one node as else this type of LLs will throw error in the line 18 as NOne.next is invalid
            return head
        
        # We need to traverse the llist once to get the last node. Nothing we can do about it
        jtr = head
        itr = jtr.next

        while itr.next: # keep going till the next node of the itr is not noe that is til the last node
            itr = itr.next
            jtr = jtr.next

        new_head = itr # makes the last node of the old LL the new head and stores it.

       
        def connections_modifier(node): # the one function to break all connection

            jtr = node
            if jtr.next is not None:
                itr = jtr.next
                while itr.next: # keep going till the next node of the itr is not none that is till the last node
                    itr = itr.next
                    jtr = jtr.next

                itr.next = jtr # last node points to the previous node
                jtr.next = None # We break the connection of the 2nd last to the last node
                connections_modifier(head)
            else:
                return
        connections_modifier(head)
        return new_head
             




        