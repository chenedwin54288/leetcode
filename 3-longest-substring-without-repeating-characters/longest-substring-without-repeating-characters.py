class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_set_len = 0
        set_start = 0
        for i in range(0, len(s)):
            if s[i] in s[set_start:i]:
                # slide the window until the previous occr of s[i]
                while s[set_start] != s[i]:
                    set_start += 1
                set_start += 1
            
            max_set_len = max(max_set_len,  i - set_start + 1)
        
        return max_set_len
            
            

        