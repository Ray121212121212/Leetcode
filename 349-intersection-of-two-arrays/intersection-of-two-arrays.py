class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        ans = []

        for _ in set1:
            if _ in set2:
                ans.append(_)
        
        return ans

    
        