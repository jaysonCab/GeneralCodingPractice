# Last attempted December 8th 2024

# PERSONAL SOLUTION
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {
        ')': '(',
        '}': '{',
        ']': '['
        }
        newStack = []
        for item in s:
            if item == '(' or item == '{' or item == '[':
                newStack.append(item)
            elif item == '}' or item == ')' or item == ']':
                try:
                    if newStack[-1] == dictionary[item]:
                        newStack.pop()
                    else:
                        return False
                except:
                    return False
        if newStack == []:
            return True
        else:
            return False



# Easy way to check if a list is empty which is cool
# stack = []
# if stack:
#     print('Not empty')
# else:
#     print('Empty')