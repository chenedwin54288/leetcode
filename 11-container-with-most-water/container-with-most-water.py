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
        