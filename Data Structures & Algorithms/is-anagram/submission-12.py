class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        groupS, groupT = {}, {}

        for i in range(len(s)):
            groupS[s[i]] = 1 + groupS.get(s[i], 0)
            groupT[t[i]] = 1 + groupT.get(t[i], 0)
        return groupS == groupT