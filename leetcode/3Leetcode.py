# December 23rd, 2024 ||| Sliding Window Based
# Beat 6.85%, personal solution obviously slow

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest = 0
        current = 0
        setting = set()
        
        for i in range(len(s)): # i is left

            for j in range(i, len(s)):
                if s[j] not in setting: # j is right
                    current = (j-i) + 1
                    if current > biggest:
                        biggest = current
                    
                    setting.add(s[j])
                else:
                    setting.clear()
                    break
        
        return biggest
    
# ---------------------------------------------------------------------------------------------
# Proper solution | Beats like 85%

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        currentMax = 0
        sett = set()

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
                

            localMax = (right - left) + 1
            
            currentMax = max(localMax, currentMax)
            sett.add(s[right]) 

        return currentMax
    
# ------------------------------------------------------------------------------------------------
# February 15th, 2025
# Personal solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        left = 0
        right = 0
        count = 0

        while right < len(s):
            if s[right] not in sett:
                sett.add(s[right])
                right += 1
            else:
                sett.remove(s[left])
                left += 1
                
            count = max(len(sett),count)

        return count
