# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # I will use the most inefficient way to solve this question
        curr_node = head
        nodes = []
        while curr_node.next:
            #print(curr_node.val)
            nodes.append(curr_node)
            curr_node = curr_node.next
        nodes.append(curr_node)

        middle_n_index = len(nodes)/2
        if middle_n_index == 0:
            head = None
        elif middle_n_index == len(nodes) - 1:
            nodes[middle_n_index-1].next = None
        else:
            nodes[middle_n_index - 1].next = nodes[middle_n_index + 1]

        return head
