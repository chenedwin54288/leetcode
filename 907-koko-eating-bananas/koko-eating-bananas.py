class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # - h will be >= len(piles)
        # - we can use binary search to gradually change 
        #   the value of k
        # - the starting search range will be 
        #   min_k = 1
        #   max_k = max(piles)

        # [3,6,7,11] h = 8
        # min_k = 1, max_k = 11 => k = 6
        # 1 + 1 + 2 + 2 == 6
        # min_k = 1, max_k = 5 => k = 3
        # 1 + 2 + 2 + 3 == 8 
        # min_k = 1, max_k = 2 => k = 2
        # 2 + 3 + 4 + 6 == 15
        # min_k = 3, max_k = 2 => k = 3 

        # [30,11,23,4,20] h = 5
        # min_k = 1, max_k = 30 => k = 16
        # 3 + 1 + 2 + 1 + 2 == 9
        # min_k = 17, max_k = 30 => k = 24
        # 2 + 1 + 1 + 1 + 1 == 6
        # min_k = 25, max_k = 30 => k = 28
        # 2 + 1 + 1 + 1 + 1 == 6
        # min_k = 29, max_k = 30 => k = 30
        # 1 + 1 + 1 + 1 + 1 == 5
        # min_k = 31, max_k = 30 => k = 31...STOP 

        # [2,2] h = 4
        # min_k = 1, max_k = 2 => k = 2
        # 1 + 1 == 2
        # min_k = 1, max_k = 1 => k = 1... STOP

        def calc_time(k):
            total_time = 0
            for p in piles:
                total_time += (p + k - 1) // k
            return total_time
            

        low = 1
        high = max(piles)
        
    
        while low < high:
            k = (low + high) // 2
            
            # Optimized compute_time logic using math.ceil
            total_time = calc_time(k)
            
            if total_time <= h:
                # If we finished in time, k might be the answer, 
                # but there could be a smaller k. So we keep k in range.
                high = k
            else:
                # If we didn't finish in time, k is too small. 
                # We must go higher than k.
                low = k + 1
            
        return low
            


                

        