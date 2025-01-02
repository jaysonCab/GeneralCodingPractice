from collections import Counter

class Solution:
    def permutation(self, s1, s2):
        if len(s1) != len(s2):
            return 0
        if Counter(s1) == Counter(s2):
            return 1
        else:
            return 0

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window = ''
        for i in range(len(s1)):
            window += s2[i]

        correct = self.permutation(s1, window)
        if correct == 1:
            return True
        else:

            for i in range(len(s1), len(s2)):
                window = window[1:]
                window += s2[i]
                correct = self.permutation(s1, window)

                if correct == 1:
                    return True
        return False