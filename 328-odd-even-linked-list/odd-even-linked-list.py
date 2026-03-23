# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head:
            return 

        odd_start_node = head.next
        even_end_node = head
        curr_node = head
        index = 0
        while curr_node:
            next_node = curr_node.next
            if index % 2 == 0:
                # even1 -> odd1 -> even2
                if curr_node.next and curr_node.next.next:
                    curr_node.next = curr_node.next.next
                # even1 -> odd1
                else:
                    curr_node.next = None             
                even_end_node = curr_node
            else:
                # odd1 -> even1 -> odd2
                if curr_node.next and curr_node.next.next:
                    curr_node.next = curr_node.next.next
                # odd1 -> even1
                else:
                    curr_node.next = None 

            curr_node = next_node
            index += 1
           
        even_end_node.next = odd_start_node
        
        return head 
               
            

        