class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the count of the frequency of the numbers in the list
        #hash map to count occurences of each value
        count = {}
        #arry that is going to be the same size as input array
        #empty array and the number of empty arrays is going to be size of og arr
        freq = [[] for i in range(len(nums)+1)]
        #counting the number of time each value in nums occur
        for i in nums:
            count[i] = 1 + count.get(i,0)
        # Put number n in bucket c(count) (appears c times)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0 ,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            


        """
        bucket sort
        for each value, we are going to take an 
        input array and going to put the number of occurence
        (would be linear time if array was bounder(don't know size of array))

        a dictionary where the key I is the count(# of occurence)
        and teh value is the list of the values that occurs 

        ex [1,1,1,2,2,100]
        i(count)[0,1,2,3,4,5,6,]
        values  [[],[100],[2],[1],[]]
        top k = size of arr

        linear time bc max size of new arr is 
        the same size as the size() of input arr

        """
        