class Solution(object):
    def longestOnes(self, nums, k):
        left_pointer = 0
        num_zeros_window = 0
        max_window = 0
        
        for i in range(len(nums)):
            # 1. Expand the window: If we see a 0, count it
            if nums[i] == 0:
                num_zeros_window += 1
            
            # 2. Shrink the window: If we have too many zeros, move left pointer
            while num_zeros_window > k:
                if nums[left_pointer] == 0:
                    num_zeros_window -= 1
                left_pointer += 1
            
            # 3. Update the result
            max_window = max(max_window, i - left_pointer + 1)
               
        return max_window