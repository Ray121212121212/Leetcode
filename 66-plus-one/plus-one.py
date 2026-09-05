class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #so this is basically taking each integer in the list and incrementing it by 1
        #the thing is if the thing being incremented is 9, the list will do [1,0]
        #kk so i noticed only the last 2 indexes matter for this question
        for i in range(len(digits) - 1, -1, -1): 
            #start, stop, step)
            
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        
        return [1] + digits