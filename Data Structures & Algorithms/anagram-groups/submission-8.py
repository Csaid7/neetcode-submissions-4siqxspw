class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for item in strs:
            # 1. Create a fresh list of 26 zeros for this word
            count = [0] * 26
            
            # 2. Loop through each character in the current word
            for char in item:
                # Hint: Use ord(char) - ord('a') to get the right index (0 to 25)
                # Increment that index in your count list by 1
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(item)                
            # 3. Convert 'count' to a tuple so it can be a dictionary key,
            #    and append the ORIGINAL 'item' to it.
            
        return list(res.values())

            
