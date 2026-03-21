class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        len_gain = len(gain)
        current_alt = 0
        max_alt = 0
        for i in range(0, len_gain):
            current_alt += gain[i]
            max_alt = max(max_alt, current_alt)
        
        return max_alt 