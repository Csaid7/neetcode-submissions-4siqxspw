class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # ord()
        # a = 86
        # b = 87
        # b - a = 1
        #[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,,0,0] = b ,
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)- ord('a')] += 1 
            res[tuple(count)].append(word)
        return list(res.values())
