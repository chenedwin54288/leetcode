class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # - Since the question particularly states that
        # nums[-1] = nums[n] = -∞, there definitely exists a
        # "peak" within this range.
        
        # - The entire idea is to use binary search, starting
        # from the middle 
        #   => nums[n-1] > nums[n] > nums[n+1]
        #      ... slope going down, thus peak must exists on teh LEFT
        #   => nums[n-1] < nums[n] < nums[n+1]
        #      ... slope going up, thus peak must exist on the RIGHT
        #   => nums[n-1] < nums[n] > nums[n+1]
        #       ... peak found
        
        # - The question would not assume a case like 
        #   [1,2,3,3,3,2,1]... coz there is no peak and this is just a table


        def is_peak(index):
            if index > 0:
                if (index + 1) < len(nums) and nums[index-1] < nums[index] and nums[index] > nums[index+1]:
                    return True
                # handle   [3, {5}]   [3, 4, {5}]
                elif (index + 1) == len(nums) and nums[index-1] < nums[index]:
                    return True
            else:
                # handle   [{3}, 2]   [{3}, 2, 1]
                if (index + 1) < len(nums) and nums[index] > nums[index+1]:
                    return True
            return False

        def is_slope_up(index):
            if index > 0 and (index + 1) < len(nums):
                if nums[index-1] < nums[index] and nums[index] < nums[index+1]:
                    return True
            return False            


        current_peak = len(nums)//2 
        peak_start = 0 
        peak_end = len(nums) - 1

        while (not is_peak(current_peak) and peak_start < peak_end):
            print(peak_start, current_peak, peak_end)
            if is_slope_up(current_peak):
                peak_start = current_peak
                current_peak = (peak_end + peak_start + 1)//2 #round up 
            else:
                peak_end = current_peak
                current_peak = (peak_end + peak_start)//2 #round down
        
        return current_peak
                




        
            


