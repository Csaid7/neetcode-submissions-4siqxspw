class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] =  1 + count.get(i, 0) # { 1 : 1, 2 : 2, 3 : 3}
        for num, cnt in count.items():
            freq[cnt].append(num) #[[1],[2],[3],[],[]]

        res = []
        for i in range(len(freq) - 1, 0 , -1): # going back from greates to smallest count
            for num in freq[i]:
                res.append(num) # 
                if len(res) == k : # once the len == k meaning that we have  the most k frequent 
                    return res #

        
         

        