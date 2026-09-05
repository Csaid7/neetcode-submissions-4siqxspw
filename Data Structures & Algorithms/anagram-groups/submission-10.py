class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        # python function : ord -> a = 80 b = 81 c = 82
        # 82 - 80 = 2
        #[1,0,1,0,0,0,0,0,0,1]
        res = defaultdict(list)

        for i in strs:
            count = [0] * 26 
            for c in i:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(i) 
        return list(res.values())


        
        