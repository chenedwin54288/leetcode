class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Remember in DSE you had an encryption algorithm where
        # A, B and C shares a specific bit to their neighbours
        # which each of them use the received bits to encrypt
        # the true message. This question has similar idea

        # suppose you have 2 decimal
        # 10 xor 10        => 00
        # 10 xor 10 xor 10 => 10

        outlier = nums[0]
        for i in range(1, len(nums)):
            outlier ^= nums[i]
        return outlier 
        