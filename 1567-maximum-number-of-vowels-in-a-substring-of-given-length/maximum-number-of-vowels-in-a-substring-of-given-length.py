class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        len_s = len(s)
        max_vowels = 0
        temp_vowels = 0

        def is_vowel(input):
            if input in ["a", "e", "i", "o", "u"]:
                return True
            return False 
        
        # This question is very similar to Leetcode 643
        # Just that you have extra O(5) in each step to check whether
        # a char is a vowel or not 
        for i in range(0, len_s):  
            if i + k - 1 < len_s:
                if i - 1 >= 0:
                    temp_vowels -= 1 if is_vowel(s[i-1]) else 0
                    temp_vowels += 1 if is_vowel(s[i + k - 1]) else 0
                else:
                    for j in range(i, i+k):
                        temp_vowels += 1 if is_vowel(s[j]) else 0
                
                max_vowels = max(max_vowels, temp_vowels)

            else:
                break
        
        return max_vowels
            
            
        