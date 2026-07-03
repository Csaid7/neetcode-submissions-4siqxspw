class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # STEP 1: The Frequency Map
        # Create a dictionary to count how often each number appears.
        # Loop through 'nums' and fill it out.
        count_map = defaultdict(int)
        for i in nums:
            #[1,1,2,2,3] -> count_map = count_map[1] += 1, 1:1...1:3,
            count_map[i] += 1
        
        # STEP 2: The Buckets
        # Create a list of empty lists. The outer list needs to be size len(nums) + 1
        # Hint: buckets = [[] for _ in range(len(nums) + 1)]
        bucket =[[] for i in range(len(nums) + 1)]
        
        # STEP 3: Fill the Buckets
        # Loop through your count_map (number and its frequency).
        # Use the frequency as the index, and append the number to that bucket list.
        #.items() gives you key value pairs by going through the dictionary 
        for num, cnt in count_map.items():
            bucket[cnt].append(num)
        
        
        # STEP 4: Collect the Top K
        # Create a 'res' list. 
        # Loop through your buckets array BACKWARDS (from highest frequency to lowest).
        # Grab the numbers inside and add them to 'res' until len(res) == k.
        res = []
        for i in range(len(bucket) -1, 0, -1):
            # go through each bucket
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res


        # Return res