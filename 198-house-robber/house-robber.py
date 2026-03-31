class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [2, 1, 1] 0 -> 2
        # [2, 1, 1, 2] 0 -> 3
        # [2, 1, 1, 1, 2] 0 -> 2 -> 4

        # [2,1,1,2]
        # i = 3, rob[3] = nums[3] + max(rob[5], rob[6]) 
        #        rob[3] is 2
        # i = 2, rob[2] = nums[2] + max(rob[4], rob[5])
        #        rob[2] is 1
        # i = 1, rob[1] = nums[1] + max(rob[3], rob[4])
        #        rob[1] is 3
        # i = 0, rob[0] = nums[0] + max(rob[2], rob[3])
        #        rob[0] is 4 

        rob = [0] * (len(nums) + 3)
        for i in range(len(nums)-1, -1, -1):
            rob[i] = nums[i] + max(rob[i+2], rob[i+3])
            
        return max(rob[0], rob[1])


        
        