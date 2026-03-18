class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        first = float('inf')
        second = float('inf')
        nums_len = len(nums)
        if nums_len < 3:
            return False

        # The idea is to make "first" always take the smallest
        # and "second" take the second smallest 
        for i in range(0, nums_len):
            if first >= nums[i]:
                first = nums[i]
            # bigger than first, smaller than second 
            elif second >= nums[i]:
                second = nums[i]
            else:
                return True 
        
        return False