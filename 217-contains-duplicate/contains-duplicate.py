class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #think I should make a dictionary that counts each element and if any 
        #reaches 2, then output true but if it goes through the whole thing without
        #passing 2, then output false
        counts = {}

        for num in nums:
            if num in counts:
                return True
            counts[num] = 1
        return False
