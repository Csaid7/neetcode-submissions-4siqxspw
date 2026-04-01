class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram has same amount of letters
        #ex: act, cat. Each have a:1,c:1,t:1
        # count the amount of letters in the strings
        #use a hashmap where we are going to keep track of the key:value pairs
        #[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        # default so we don't have to deal with edge case
        res = defaultdict(list)

        for word in strs:
            count = [0]*26 
            for c in word:
                #map a to index 0 by taking ascii value of curr char 
                #and substract ascii of lower case a
                #ex: a = 80 -> 0 , 80 - 80 = 0
                # b = 81 -> , 81-80 = 1
                count[ord(c) - ord('a')] += 1
              # want to add string word | tuple non mutable
            res[tuple(count)].append(word)
        return list(res.values())

        

