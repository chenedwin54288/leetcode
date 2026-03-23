class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dig_dict = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'], 
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'], 
        }
        result = []
        def find_str(p_str, curr_dig):
            if curr_dig == len(digits):
                result.append(p_str)
                return p_str
            for c in dig_dict[digits[curr_dig]]:
                find_str(p_str + c, curr_dig+1)
            return p_str 
        
        find_str("", 0)
        return result

           
            

        
            
        