class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        count = {}
        freq = [[]for i in range(len(nums)+1)]
        # get the count
        for i in nums:
            count[i] = 1+ count.get(i,0)
        
        for num,cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            

        """"
        count of the occurence for each number in arr num 
        put the count in a list of list the len  is going to be size of nums
        in the new list the index will be teh count
        ex: [1,1,1,1,2,2,2,3]
        n,c
        list[c]=n
        [0,3,0,2,1,0,0,0]
        return the list of number that == k
        """
        