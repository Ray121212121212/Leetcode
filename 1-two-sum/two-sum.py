class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #testing 
        # Dictionary to store number -> its index
        num_to_index = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # If complement exists in our dictionary, we found the pair
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Otherwise, store current number with its index
            num_to_index[num] = i
        
        # Should never reach here if input is guaranteed to have a solution
        return []