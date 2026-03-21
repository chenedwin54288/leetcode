class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # can only have one 0 in the window
        len_nums = len(nums)
        one_deleted = False
        max_window = 0
        left_pointer = 0
        for i in range(0, len_nums):
            if nums[i] == 0 and one_deleted:
                while(nums[left_pointer] != 0):
                    left_pointer += 1
                left_pointer += 1
            elif nums[i] == 0:
                one_deleted = True 
            
            max_window = max(max_window, i - left_pointer)
        
        return max_window 

        