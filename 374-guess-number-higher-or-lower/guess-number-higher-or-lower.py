# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        current_num = n/2 + 1
        lower_range = 1
        higher_range = n

        # handle edge case
        if guess(n) == 0:
            return n

        while guess(current_num) != 0:
            # num is higher than the picked number
            if guess(current_num) == -1:
                #print("n > ans :" + str(current_num))
                higher_range = current_num
            # num is lower than the picked number
            else: 
                #print("n < ans :" + str(current_num))
                lower_range = current_num
            
            current_num = (higher_range + lower_range) / 2 
        return current_num
            

        