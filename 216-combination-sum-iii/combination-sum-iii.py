class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        # The time complexity of this question will be O(C(9,k))
        # where C(9,k) means the number of ways to choose a subset of k 
        # elements from a fixed set of 9 distinct elements
        result = []
        def find_sum(start_i, list_len, sum_l, l):
            print(start_i, list_len, sum_l, l)
            if list_len >= k:
                if sum_l == n:
                    result.append(l)
                return 
            for i in range(start_i+1, 10):
                find_sum(i, list_len+1, sum_l+i, l + [i])
        
        find_sum(0, 0, 0, [])
        return result
                



        