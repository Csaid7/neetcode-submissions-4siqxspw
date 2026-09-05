class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        keep track of frequency of the numebr
        {
            1:1,
            2:2,
            3:3
        }
        use a freq list
        index == frequectcy and 
        [1,2,3]
        """
        # idk lol but let's get started

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # get the freq count
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
            # ex : 1:1,2:0..1..2,.......
        for val, num in count.items():
            freq[num].append(val)
            #ex : [[]]
        res = [] # append the result
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                res.append(n)
        return res

        


        