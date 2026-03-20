class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        len_nums = len(nums)
        maximum_average = float(nums[0]) if len_nums == 1 else float('-inf') 
        temp_sum = 0
        for i in range(0, len_nums):   
            # [1,12,{-5,-6,50,3}] i=2 
            # 2 + 4 = 6 < 6
            # 2 + 4 - 1 = 5 < 6
            if i + k - 1 < len_nums:
                # Making it faster by taking out the "left_most" and adding back "right_most"
                # 1 + 12 -5 -6
                #     12 -5 -6 + 50
                #        -5 -6 + 50 + 3
                if i - 1 >= 0:
                    temp_sum -= nums[i - 1]
                    temp_sum += nums[i + k - 1]
                else:
                    temp_sum = sum(nums[i:i+k])
                
                new_average = temp_sum / float(k)
                maximum_average = max(maximum_average, new_average)

                #print(i, new_average, nums[i:i+k])
            else:
                break

        
        
        return maximum_average
            
