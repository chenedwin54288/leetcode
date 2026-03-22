import heapq
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         temp = [-n for n in nums]
#         heapq.heapify(temp)
#         k_th_largest = 0
#         for i in range(k):
#             k_th_largest = -heapq.heappop(temp)
#         return k_th_largest



class Solution(object):
    def findKthLargest(self, nums, k):
        # Maintain a min-heap of size k
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root is the k-th largest
        return min_heap[0]
        