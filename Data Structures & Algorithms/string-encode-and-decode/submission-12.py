class Solution:

    def encode(self, strs: List[str]) -> str:

        res =""
        for i in strs:
            res += str(len(i)) + "|" + i
        return res


        

    def decode(self, s: str) -> List[str]:# 5|Hello3run
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "|":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            str_ = s[start:end]
            res.append(str_)
            i = end
        return res
            
