class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        #testing again
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare prefix with each string in the array
        for string in strs[1:]:
            # Shrink prefix until it matches the beginning of current string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Remove last character
                if not prefix:
                    return ""
        
        return prefix