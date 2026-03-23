# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # In efficient, but put the stuff in the linked-list
        # to a list (so we know the end and start)
        # => if we know the linked-list length beforehand, it might be easier
        red_list = []
        curr_node = head
        max_sum = 0
        while curr_node:
            red_list.append(curr_node)
            curr_node = curr_node.next

        
        i = 0
        j = len(red_list) - 1
        while i < j:
            max_sum = max(max_sum, red_list[i].val + red_list[j].val) 
            i += 1
            j -= 1
        
        return max_sum