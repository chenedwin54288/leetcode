class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = [0] * len(nums)
        list_len = len(nums)

        # compute product 
        product = 1
        for i in range(0, list_len):
            product *= nums[i]

        # just do division (exclude), becareful for 0
        for i in range(0, list_len):
            if nums[i] == 0:
                product_edge = 1
                for j in range(0, list_len):
                    if j != i:
                        product_edge *= nums[j]
                output[i] = product_edge        
            else:
                output[i] = product / nums[i]
        
        return output


                
            
        