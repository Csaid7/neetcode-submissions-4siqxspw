class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "|" +  i 
        return res

    def decode(self, s: str) -> List[str]:
        #5|Hello5|World
        # look for "|"
            # once that is foudn slice the number and store it
            #\
        res = []
        i = 0
        while i < len(s):
            j = i
            # move the pointer if we have not yet found the delimter
            while s[j] != "|":
                j += 1 
            # extract the length of the word 
            length = int(s[i:j])
            # point i to the first letter
            i = j + 1
            j = length + i
            new_w = s[i:j]
            res.append(new_w)
            # update the pointer
            i = j
        return res


