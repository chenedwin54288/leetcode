import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        temp = [-n for n in nums]
        heapq.heapify(temp)
        k_th_largest = 0
        for i in range(k):
            k_th_largest = -heapq.heappop(temp)
        return k_th_largest
        