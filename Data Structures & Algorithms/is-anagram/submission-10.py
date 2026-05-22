class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # same number of char
        #  count num of char in each str
        # compare it and if same frequency then it is an anagram
        # k
        if len(s) != len(t):
            return False
        countT = {}
        countS = {}

        for i in range(len(s)):
            countT[s[i]] = 1 + countT.get(s[i],0)
            countS[t[i]] = 1 + countS.get(t[i],0)
        if countT == countS:
            return True
        else:
            return False

    


    