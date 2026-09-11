class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #for this problem, we utilize xor's properties, 0 xor any number is that number
        #we iterate through nums and xor each number. In binary, all duplicates will cancel each other out, hence leaving the single number as the answer
        ans = 0

        for num in nums:
            ans ^= num

        return ans