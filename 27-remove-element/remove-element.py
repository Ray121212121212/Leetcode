class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[k] = nums[x]
                k += 1
        return k
