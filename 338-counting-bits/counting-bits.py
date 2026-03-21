class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 0 0
        # 1 1

        # 2 10
        # 3 11

        # 4 100
        # 5 101
        # 6 110
        # 7 111

        # 8   1000 (1)
        # 9   1001 (2)
        # 10  1010 (2)
        # 11  1011 (3)
        # 12  1100 (2)
        # 13  1101 (3)
        # 14  1110 (3)
        # 15  1111 (4)

        # O(n*W) solution
        return_list = [0]*(n+1)
        for i in range(n+1):
            bit_count = 0
            for b in range(32):
                if 1 & (i >> b):
                    bit_count += 1
            return_list[i] = bit_count
        return return_list 


        
             

