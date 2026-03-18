class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count = n
       
        # for edge case [0] or [1]
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        #sliding window maybe a better solution 
        #O(n)
        for i in range(0, len(flowerbed)):
            # start
            if n > 0:
                if i == 0:
                    if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1 
                        n -= 1
                # end
                elif i == len(flowerbed) - 1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -= 1

                # sliding window size [3]
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
        
        return n == 0

