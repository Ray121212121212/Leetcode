class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
            # p1 points to the last REAL element in nums1
        # We use m - 1 because indexes start at 0
        p1 = m - 1

        # p2 points to the last element in nums2
        p2 = n - 1

        # p points to the last position in nums1
        # This is where we will put the largest element
        p = m + n - 1

        # Keep comparing elements as long as
        # both arrays still have elements left
        while p1 >= 0 and p2 >= 0:

            # Compare the largest remaining elements
            # from nums1 and nums2
            if nums1[p1] > nums2[p2]:

                # nums1's element is bigger,
                # so put it at the back of nums1
                nums1[p] = nums1[p1]

                # Move p1 backwards to the next element
                p1 -= 1

            else:

                # nums2's element is bigger (or equal),
                # so put it at the back of nums1
                nums1[p] = nums2[p2]

                # Move p2 backwards to the next element
                p2 -= 1

            # Move the position where we are inserting backwards
            p -= 1

        # If nums2 still has elements left,
        # copy them into nums1
        #
        # We don't need a similar loop for nums1 because
        # any remaining nums1 elements are already in the
        # correct position.
        while p2 >= 0:

            nums1[p] = nums2[p2]

            # Move backwards through nums2
            p2 -= 1

            # Move backwards through nums1
            p -= 1