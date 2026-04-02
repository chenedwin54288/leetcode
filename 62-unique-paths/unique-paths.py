class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Solution1: 2D DP
        # solu = [[0]*n]*m
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0:
        #             solu[i][j] = 1
        #         else:
        #             solu[i][j] = solu[i][j-1] + solu[i-1][j]
        
        # return solu[m-1][n-1]


        # Solution2: Think it in a math way
        # I think I need to review Combinatorics
        # - when you have m x n grid and you can only move R or L
        # - to reach dest, you will have m+n-2 steps
        # - out of these m+n-2 steps, you can randomly choose n-1 R steps
        # - thus the number of unique steps are C(m+n-2, n-1)
        import operator as op
        from functools import reduce

        def ncr(n, r):
            r = min(r, n-r)
            numer = reduce(op.mul, range(n, n-r, -1), 1)
            denom = reduce(op.mul, range(1, r+1), 1)
            return numer // denom  # or / in Python 2
        
        return ncr(m+n-2, n-1)

       

        
        
        