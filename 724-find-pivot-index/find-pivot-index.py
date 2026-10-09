class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = 0
        for x in range(len(nums)):
            leftsum = sum(nums[:x])
            rightsum = sum(nums[x+1:])
            if leftsum == rightsum:
                return x
        return -1

                




            

        