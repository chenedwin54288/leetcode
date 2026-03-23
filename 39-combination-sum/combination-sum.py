class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def find_sum(p_sum, l, index):
            if p_sum < target:
                for j in range(0, len(candidates)):
                    if index <= j:
                         find_sum(p_sum + candidates[j], l + [candidates[j]], j)
                return 
            elif p_sum > target:
                return
            else: # p_sum == target
                # sorted_l = sorted(l)

                # # very inefficient, ensuring uniqueness
                # if sorted_l not in result:
                result.append(l)
        
        find_sum(0, [], 0)
        return result