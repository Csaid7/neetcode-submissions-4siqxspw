class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        #|5hello|5World|4five|
        for i in strs:
            res +=  str(len(i)) + "|"  + i  
        return res 

    def decode(self, s: str) -> List[str]:
        # 5|hello5|World4|five|
        res = []
        i = 0
        while i != len(s) :
            j = i
            while s[j] != "|":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            new_str = s[start:end]
            res.append(new_str)
            i = end
        return res





