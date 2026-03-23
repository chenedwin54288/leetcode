# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_node = None 
        curr_node = head
        next_node = head
        while next_node:
            # 1 -> 2 -> 3
            # curr_node = 1
            curr_node = next_node
            # next_node = 2
            next_node = next_node.next
            # 1 -> None
            curr_node.next = prev_node

            # if prev_node and next_node:
            #     print(prev_node.val, curr_node.val, next_node.val)
        
            # prev_node = 1
            prev_node = curr_node
        
        return prev_node 
            