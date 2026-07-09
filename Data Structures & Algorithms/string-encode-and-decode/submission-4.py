class Solution:

    def encode(self, strs: List[str]) -> str:
        # list of strings and return one single encoded strings
        # we can use a limiter like "|" to separate the wrods
        # if the limiter has  a "|" we can use the length of the strings as an extra one
        # list = "word","dork","ford","quirk"
        # res = 4|word|4dork|4ford|5quirk
        res = ""
        for word in strs:
            res +=  str(len(word)) +"|" + word
        return res 


    def decode(self, s: str) -> List[str]:
        #res = 4|word|4dork|4ford|5quirk
        res = []
        i = 0
        #using while since we need the pointer to jump around
        # go through the string
        while i < len(s):
            j = i 
            while s[j] != "|":
                j += 1
            # 2. Extract the length number from between 'i' and 'j'
            # Hint: length = int(s[i:j])
            length = int(s[i:j])
            # 3. Slice the actual word out of the string! 
            # The word starts right after the '|' (which is j + 1)
            # and ends after its total length.
            i = j + 1
            j =  i + length
            new_word = s[i:j]

            # 4. Append that word to your 'res' list
            res.append(new_word)
            # 5. THE JUMP: Move your pointer 'i' to the start of the next item
            # Hint: i = j + 1 + length
            i = j
        return res


