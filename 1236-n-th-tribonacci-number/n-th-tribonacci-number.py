class Solution(object):
    def tribonacci_rec(self, n):
        if n <= 1:
            return n
        if n == 2:
            return 1

        if self.d[n] == -1:
            self.d[n] = self.tribonacci_rec(n-1) + self.tribonacci_rec(n-2) + self.tribonacci_rec(n-3)
        
        return self.d[n]

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 0 
        # 0 1 
        # 0 1 1
        # 0 1 1 2
        # 0 1 1 2 4
        # 0 1 1 2 4 7 

        self.d = [-1]*(n+1)

        return self.tribonacci_rec(n)

        

       
        

