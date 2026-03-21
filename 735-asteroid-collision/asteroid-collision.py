class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        def will_crash(ast1, ast2):
            return abs(ast1) == ast1 and not (abs(ast2) == ast2)

        def crash(ast1, ast2):
            if abs(ast1) > abs(ast2):
                return ast1
            elif abs(ast1) < abs(ast2):
                return ast2
            else:
                return 0 

        stack = []
        for i in range(0, len(asteroids)):
            crash_result = asteroids[i]
            while(len(stack) > 0 and will_crash(stack[-1], asteroids[i])):
                crash_result = crash(asteroids[i], stack[-1])
                if crash_result == asteroids[i]:
                    stack.pop()
                elif crash_result == stack[-1]:
                    break
                else:
                    stack.pop()
                    break
            
            if crash_result == asteroids[i]:
                stack.append(crash_result)
        
        return stack

           
                