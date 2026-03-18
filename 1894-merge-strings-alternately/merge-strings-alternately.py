class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        longer_word = word1 if len(word1) >= len(word2) else word2
        return_list = ""
        for i in range(0, len(longer_word)):
            if i < len(word1):
                return_list += word1[i]
            if i < len(word2):
                return_list += word2[i]
        
        return return_list




        