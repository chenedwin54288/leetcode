class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
    
        # O(n*W) solution
        # return_list = [0]*(n+1)
        # for i in range(n+1):
        #     bit_count = 0
        #     for b in range(32):
        #         if 1 & (i >> b):
        #             bit_count += 1
        #     return_list[i] = bit_count
        # return return_list 

        # O(nlogn) solution
        # using DP
        # 0 0
        # 1 1... 1 + dp[n-1]

        # 2 10... 1 + dp[n-2]
        # 3 11... 1 + dp[n-2]

        # 4 100... 1 + dp[n-4]
        # 5 101... 1 + dp[n-4]
        # 6 110
        # 7 111

        # 8   1000 (1)... 1 + dp[n-8]
        # 9   1001 (2)... 1 + dp[n-8]
        # 10  1010 (2)
        # 11  1011 (3)
        # 12  1100 (2)
        # 13  1101 (3)
        # 14  1110 (3)
        # 15  1111 (4)
        # N   ... dp[N] = 1 + dp[N-offset]
        dp = [0]*(n+1)
        offset = 1
        for i in range(1, n+1):
            if i == 0:
                dp[i] = 0
            
            # i = 1, offset=1
            # i = 2, offset=2
            # i = 3, offset=2
            # i = 4, offset=4
            #...
            if offset*2 == i:
                offset = i
            
            dp[i] = 1 + dp[i-offset]
        
        return dp
            





        
             

