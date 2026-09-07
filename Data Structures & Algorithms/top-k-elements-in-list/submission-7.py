class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]  for i in range(len(nums) + 1)]

        # get the count in the hashmap
        for num in nums:
            count[num] = 1 + count.get(num, 0 )
        
        # store the freq as index
        for i, val in  (count.items()):
            freq[val].append(i)# append the val/num to the index[[1],[2],[3]]
        
        res = []
        for i in range(len(freq) - 1, -1 , -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res
                
        return []
                