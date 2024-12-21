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

# ------------------------------------------------------------------------------------------------
# December 21st, done with strings instead of lists

class Solution:
    def isValid(self, s: str) -> bool:
        
        dictionary = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        newStack = ''

        for item in s:
            if item == '{' or item == '(' or item == '[':
                newStack += item
            else:
                try:
                    if newStack[-1] != dictionary[item]:
                        return False
                    else:
                        newStack = newStack[:-1]
                except:
                    return False
        
        if len(newStack) != 0:
            return False

        return True
                