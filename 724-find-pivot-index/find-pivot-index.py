class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        r_total = 0
        l_total = sum(nums)
        
        # [{1},7,3,6,5,6] 28, pivot 0
        # [1,{7},3,6,5,6] 28 - 1 - 7, pivot 1
        # [1,7,{3},6,5,6] 28 - 1 - 7 - 3, pivot 2 

        for pivot in range(0, len_nums):
            if pivot > 0:
                r_total += nums[pivot - 1]
                l_total -= nums[pivot]
            print(pivot, r_total, l_total)

            if pivot == 0:
                l_total -= nums[pivot]

            if r_total == l_total:
                return pivot

            

        return -1
                

        

            
        
        