class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1_map = {}
        nums2_map = {}
        for i in nums1:
            nums1_map[i] = 0
        for j in nums2:    
            nums2_map[j] = 0
        
        nums1_list = []
        nums2_list = []
        for i in nums1_map:
            if i not in nums2_map:
                nums1_list.append(i)
        for j in nums2_map:
            if j not in nums1_map:
                nums2_list.append(j)
        
        return [nums1_list, nums2_list]
            
                
          

        