class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortedS = "".join(sorted(s))
        sorteddT = "".join(sorted(t))
        return sortedS == sorteddT
        