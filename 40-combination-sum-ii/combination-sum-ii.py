class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort() # Critical for skipping duplicates

        def find_comb(p_sum, index, current_list):
            if p_sum == target:
                result.append(list(current_list))
                return
            if p_sum > target:
                return

            if p_sum > target:
                return 

            for j in range(index, len(candidates)):
                # If this number is the same as the previous one at THIS level, skip it
                # [10,1,2,7,6,1,5]
                # sorted is...[1,1,2,5,6,7,10]
                # 1->2->5
                # 1->2->5 two possible comb for sum == 8
                # 'j > index' ensures we don't skip the very first occurrence
                if j > index and candidates[j] == candidates[j-1]:
                    continue
                
                find_comb(p_sum + candidates[j], j + 1, current_list+[candidates[j]])
    
        find_comb(0, 0, [])
        return result
            
            
        