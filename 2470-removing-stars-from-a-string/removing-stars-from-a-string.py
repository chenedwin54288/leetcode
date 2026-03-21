class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        len_s = len(s)
        for i in range(0, len_s):
            if s[i] == '*' and len(stack) > 0:
                stack.pop()
            else:
                # push to the stack
                stack.append(s[i])
        
        return "".join(stack)
            

        