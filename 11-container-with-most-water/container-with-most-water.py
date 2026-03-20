class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        len_height = len(height)
        left_pointer = 0
        right_pointer = len_height - 1
        max_area = 0

        # Below is an O(n) solution
        # - if you think about it, your container can only contain 
        #   min{height[l_p], height[r_p]} * (r_p - l_p)
        # - so if you take two pointers from both side and gradually compute
        #   the inner containers, you could get the maximum possible container
        while(left_pointer != right_pointer):
            if height[left_pointer] < height[right_pointer]:
                max_area = max(max_area, height[left_pointer] * (right_pointer - left_pointer))
                left_pointer += 1
            elif height[left_pointer] > height[right_pointer]:
                max_area = max(max_area, height[right_pointer] * (right_pointer - left_pointer))
                right_pointer -= 1
            else:
                max_area = max(max_area, height[left_pointer] * (right_pointer - left_pointer))
                left_pointer += 1

        return max_area
        