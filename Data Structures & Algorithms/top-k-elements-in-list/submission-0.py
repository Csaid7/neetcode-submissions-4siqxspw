class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#example:Input: nums = [1,2,2,3,3,3], k = 2

#Output: [2,3]
        count = {}
        #creates an empty list with the size being the length of the list
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            # add the number of occurence to the int in the list
            # if num is already in the list(count.get(num,0)) get its current count else return 0
            count[i] = 1 + count.get(i,0)# count = {1:1,2:2}
        #now we are going to group items by frequency
        for i, j in count.items():# count.items gives key value pairs
        # shows the frequency of the number, how many times did the number appear once(1),twice(2),thrice(3)
            freq[j].append(i)#freq[j] get the count and append its number
        #storing result
        res = []
        #start at highest frequency, go down to 1(not 0)(-1 goes backward)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
             
                   
            
        