class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

         seen = set()# creating a hash set
         for num in nums:
            if num in seen:
                return True
            seen.add(num)
         return False 
        
        
         