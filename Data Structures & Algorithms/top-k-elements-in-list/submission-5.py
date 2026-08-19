class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # dictionary : [1:1,2:2,3:3]
        freq = [[] for i in range(len(nums) + 1)]

        for c in nums:
            count[c] = 1 + count.get(c,0)
        
        for i, num in count.items():
            freq[num].append(i)

        res = []
        for i in range(len(freq)-1,0,-1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res
                

            
