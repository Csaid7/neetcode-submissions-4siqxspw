class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):# if the len of the strings are not the same
        # return false because it defies the definition of an anogram
            return False
        countS,countT= {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT

        

        