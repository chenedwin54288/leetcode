class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(" ")
        s_list.reverse()
        s_list = [s for s in s_list if s != '']
        return " ".join(s_list)
        