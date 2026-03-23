class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def find_sum(p_sum, l):
            if p_sum < target:
                for j in candidates:
                    l.append(j)
                    find_sum(p_sum+j, l)
                    l.pop()
                return 
            elif p_sum > target:
                return
            else: # p_sum == target
                sorted_l = sorted(l)
                if sorted_l not in result:
                    result.append(sorted_l)
        
        find_sum(0, [])
        return result