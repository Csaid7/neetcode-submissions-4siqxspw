class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Changing from a set() to a dictionary {}
        # This will store { number_we_saw : its_index }
        seen = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            # Check if the complement is already in our dictionary
            if diff in seen:
                # seen[diff] gives us the index of the complement
                return [seen[diff], i]
            
            # If not found, store the current number and its index
            seen[n] = i
            
        return []
