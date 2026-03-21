class Solution(object):
 
    def is_digit(self, s):
        if s in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return True
        return False 

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(s):
            print(i)
            if s[i] == "]":
                reverse_stack = []
                while stack[-1] != "[":
                    reverse_stack.append(stack.pop())
                reverse_stack.reverse()
                stack.pop() # get rid of "["
                str_count = int(stack.pop()) # now get the int
                stack.append("".join(reverse_stack) * str_count)
            # Take into account 1,2,3 digit numbers
            elif self.is_digit(s[i]):
                digit = s[i]
                while self.is_digit(s[i + 1]):
                    i += 1
                    digit += s[i] 
                stack.append(digit)
            else:
                stack.append(s[i])
            
            i+=1
        return "".join(stack)
                
        