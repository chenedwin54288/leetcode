class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        solu = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    solu[i][j] = 1
                else:
                    solu[i][j] = solu[i][j-1] + solu[i-1][j]
        
        return solu[m-1][n-1]
       

        
        
        