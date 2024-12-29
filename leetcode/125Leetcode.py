class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        sett = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}

        while left < right:
            if s[left] == s[right] and s[left] in sett and s[right] in sett:
                left += 1
                right -= 1
            elif s[left] not in sett:
                left += 1
            elif s[right] not in sett:
                right -= 1
            else:
                return False

        return True