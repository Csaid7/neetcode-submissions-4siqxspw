class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):# if the len of the strings are not the same
        # return false because it defies the definition of an anogram
            return False
        #return true or false if they are equal or not
        return sorted(s) == sorted(t)
        

        