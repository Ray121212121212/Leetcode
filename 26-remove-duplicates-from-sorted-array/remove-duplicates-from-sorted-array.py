class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Non decreasing order simply means ascending order
        # return number of unique values, update the array
        # gonna use 2 pointers to solve
        p1 = 1
        for _ in range(1, len(nums)):
            if nums[_] != nums[_-1]: #checks if they are unique
                nums[p1] = nums[_]   #changes elemnt if it is
                p1 += 1  #increments to next pointer
        return p1


        