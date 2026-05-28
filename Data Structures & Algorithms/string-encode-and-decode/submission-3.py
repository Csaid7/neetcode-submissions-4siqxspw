class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i)) + "|" + i # 4!word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        while i < len(s):
            j = i 
            while s[j] != "|":
                j += 1 
            lens = int(s[i:j]) # length of string
            # we are going to slice at j+1(where the first letter starts) to end of length of the word (j+1) + lens
            i = j + 1 # first letter of the word after the delimitter
            j = i + lens # last letter of word[j] 
            res.append(s[i:j]) 
            #to 
            i = j
        return res


        
        

        
