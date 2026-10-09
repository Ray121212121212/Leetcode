class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = 0
        for x in range(len(nums)):
            if sum(nums[:x]) == sum(nums[x+1:]):
                return x
            #leftsum = sum(nums[:x])
            #rightsum = sum(nums[x+1:])
            #if leftsum == rightsum:   
        return -1

                




            

        