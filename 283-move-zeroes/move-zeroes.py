class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        start_p = 0
        for i in range(0, nums_len):
            if nums[i] != 0:
                nums[start_p] = nums[i]
                start_p += 1
        
        for j in range(nums_len-1, start_p-1, -1):
            nums[j] = 0
                    
        