class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occur_map = {}
        occur = [[] for i in range(len(arr)+1)] 
        for i in arr:
            occur_map[i] = 1 + occur_map.get(i, 0)
        
        for ele in occur_map:
            print(occur, occur_map[ele], ele)
            occur[occur_map[ele]].append(ele)
            if len(occur[occur_map[ele]]) > 1:
                return False
        
        return True
        
