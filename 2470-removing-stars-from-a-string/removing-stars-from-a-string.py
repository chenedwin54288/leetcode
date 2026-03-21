class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(0, len(s)):
            if s[i] == '*' and len(stack) > 0:
                stack.pop()
            else:
                # push to the stack
                stack.append(s[i])
        
        return "".join(stack)
            

        