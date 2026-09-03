class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for x in range(len(nums)):
            if nums[x] >= target:
                return x
        return len(nums)
        #if it doesn't find the target, we automatically add it to the end