class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        len_nums = len(nums)
        k_sum_counter = 0

        # Python dict performance:
        # - creating a dict from N elements: O(N)
        # - fetch & insert: O(1)
        track_usage = {}
        for i in range(0, len_nums):
            if nums[i] not in track_usage:
                track_usage[nums[i]] = 1
            else: 
                track_usage[nums[i]] += 1
        
        
        for j in range(0, len_nums):
            to_find = k - nums[j] 
            if to_find in track_usage:
                if track_usage[to_find] <= 0 or track_usage[nums[j]] <= 0: 
                    continue
                elif to_find == nums[j] and track_usage[to_find] <= 1:
                    continue 
                else:
                    track_usage[to_find] -= 1
                    track_usage[nums[j]] -= 1  
                    k_sum_counter += 1
        
        return k_sum_counter
        