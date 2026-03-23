class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for brack in s:
            stack.append(brack)

            if len(stack) > 1 and (brack == ")" or brack == "]" or brack == "}"): 
                stack.pop()
                prev_brack = stack.pop()
                print(prev_brack, brack)
                if prev_brack == "(" and brack == ")":  
                    continue                
                elif prev_brack == "[" and brack == "]":
                    continue
                elif prev_brack == "{" and brack == "}":
                    continue
                else:
                    return False
        
        return len(stack) == 0