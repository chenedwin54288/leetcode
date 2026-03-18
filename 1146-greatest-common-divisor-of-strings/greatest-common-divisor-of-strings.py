class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
    
        # The time complexity of this algorithm is min(n, m) * (n + m)
        shorter_str = str1 if len(str1) <= len(str2) else str2
        longer_str = str2 if len(str1) <= len(str2) else str1

        def isDivisor(str1, str2, div):
            if len(str1) % len(div) == 0 and len(str2) % len(div) == 0:    
                mul_1 = len(str1) / len(div)
                mul_2 = len(str2) / len(div)
                est_str1 = div * mul_1
                est_str2 = div * mul_2
                return est_str1 == str1 and est_str2 == str2
            return False
            
        for i in range(len(shorter_str), 0, -1):
            div = shorter_str[:i]

            if isDivisor(shorter_str, longer_str, div):
                return div
        return ""
                
            

        