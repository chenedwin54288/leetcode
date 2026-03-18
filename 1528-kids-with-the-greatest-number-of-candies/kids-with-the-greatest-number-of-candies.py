class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        # This solution is O(n)
        # You don't need to get max() in every loop that will
        # make the solution O(n^2)`
        result = [False] * len(candies)
        max_candy = max(candies)

        for i in range(0, len(candies)):
            if max_candy <= candies[i] + extraCandies:
                result[i] = True
        return result
                
            
        