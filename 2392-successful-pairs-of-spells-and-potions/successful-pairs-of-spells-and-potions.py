class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
 
        sorted_array = sorted(potions)
        return_array = [0] * len(spells)

        def find_min_index(search_for):
            low = 0
            high = len(sorted_array)
            
            while low < high:
                mid = (low + high) // 2
                if sorted_array[mid] < search_for:
                    low = mid + 1
                else:
                    high = mid
                    
            return low


        for i in range(0, len(spells)):
            search_for = 0
            if success % spells[i] != 0:
                search_for = success/spells[i] + 1
            else:
                search_for = success/spells[i]

            # can be O(logN)?
            return_array[i] += (len(sorted_array) - find_min_index(search_for))
    
        return return_array
            


            