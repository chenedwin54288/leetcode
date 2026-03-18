class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        str_ret = ""
        for i in range(0, len(s)):
            if lower(s[i]) == "a" or lower(s[i]) == "e" or lower(s[i]) == "i" or lower(s[i]) == "o" or lower(s[i]) == "u":
                vowels.append(s[i])
        
        vowels.reverse()
        j = 0
        for i in range(0, len(s)):
            if lower(s[i]) == "a" or lower(s[i]) == "e" or lower(s[i]) == "i" or lower(s[i]) == "o" or lower(s[i]) == "u":
                # you cannot do s[i] = vowels[j], as string is immutable in Python
                str_ret += vowels[j]
                j += 1
            else:
                str_ret += s[i]

        return str_ret

        
        