class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # 1000
        # 0011
        # 0101
        bit_flip = 0
        for i in range(32):
            # only get the least significant bit
            curr_a = (a >> i) & 1 
            curr_b = (b >> i) & 1 
            curr_c = (c >> i) & 1

            if (curr_a | curr_b) != curr_c:
                print(curr_a, curr_b, curr_c)
                if curr_a != curr_b:
                    bit_flip += 1
                else:
                    if curr_c: 
                        bit_flip += 1
                    else:
                        bit_flip += 2
        
        return bit_flip
        