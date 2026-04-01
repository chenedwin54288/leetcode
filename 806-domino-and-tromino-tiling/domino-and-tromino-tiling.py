class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        full = [0]*(n+1)
        top_miss = [0]*(n+1)
        bot_miss = [0]*(n+1)
        
        # when n == 1
        full[1] = 1

        # when n == 2
        if n >= 2:
            full[2] = 2
            top_miss[2] = 1
            bot_miss[2] = 1 
        
        if n >= 3:
            for i in range(3, n+1):
                full[i] = full[i-1] + full[i-2] + top_miss[i-1] + bot_miss[i-1]
                top_miss[i] = full[i-2] + bot_miss[i-1]
                bot_miss[i] = full[i-2] + top_miss[i-1]
        
        return full[n] % 1000000007


        