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
                    find_sum(p_sum+j, l+[j])
                return 
            elif p_sum > target:
                return
            else: # p_sum == target
                sorted_l = sorted(l)

                # very inefficient, ensuring uniqueness
                if sorted_l not in result:
                    result.append(sorted_l)
        
        find_sum(0, [])
        return result