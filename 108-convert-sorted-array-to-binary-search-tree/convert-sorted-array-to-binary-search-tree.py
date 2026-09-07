# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # Helper function to perform recursive construction
        # Uses left and right pointers to avoid slicing (which creates new arrays)
        def helper(left, right):
            # Base case: if left pointer exceeds right, no elements to process
            if left > right:
                return None
            
            # Choose the middle element as the root
            # Using (left + right) // 2 gives us the left-middle for even-length arrays
            # This helps maintain balance
            mid = (left + right) // 2
            
            # Create a new TreeNode with the middle value
            root = TreeNode(nums[mid])
            
            # Recursively build the left subtree using elements left of mid
            # The left subtree will contain elements from left to mid-1
            root.left = helper(left, mid - 1)
            
            # Recursively build the right subtree using elements right of mid
            # The right subtree will contain elements from mid+1 to right
            root.right = helper(mid + 1, right)
            
            # Return the root of this subtree
            return root
        
        # Start the recursive construction with the full array range
        return helper(0, len(nums) - 1)