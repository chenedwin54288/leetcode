class Solution(object):



    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        subseq_len = len(s)
        tosearch_len = len(t)
        subseq_mark = [-1] * subseq_len
        next_search = 0

        # Note: an empty string is considered a subsequence of everything
        if s == "":
            return True 
        if t == "":
            return False

        # if subseq_len == 1 and subseq_len == 1:
        #     if t[0] == s[0]:
        #         return True
        #     else:
        #         return False
        
        for i in range(0, tosearch_len):
            if t[i] == s[next_search]:
                subseq_mark[next_search] = i
                next_search += 1
            if next_search == subseq_len:
                return True
        
        return False

