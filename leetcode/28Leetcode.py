# # TESTING

# haystack = 'sadbutsad'
# needle = 'sad'

# new = ''

# for i in range(len(haystack)):
#     new += haystack[i]

#     if new[-len(needle):] == needle:
#         print(i-len(needle)+1)

# ---------------------------------------------------------------------

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        checkString = ''
    
        for i in range(len(haystack)):
            checkString += haystack[i]

            if checkString[-len(needle):] == needle:
                return i-len(needle)+1

        return -1