class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Note: Think from the back!!!
        # [10,15,20]
        # i = 2, short[2] = min(20)
        # i = 1, short[1] = min(15+short[2], 15+short[3])... short[3] is 0
        # i = 0, short[0] = min(10+short[1], 10+short[2])

        short = [0] * (len(cost)+2)
        for i in range(len(cost)-1, -1, -1):
            short[i] = min(cost[i]+short[i+1], cost[i]+short[i+2])
        
        return min(short[0], short[1])