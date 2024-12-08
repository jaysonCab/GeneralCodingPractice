#Last attempted December 7th 2024

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        xTransform = str(x)
        newString = xTransform[::-1]
        
        if newString == xTransform:
            return True
        else:
            return False
