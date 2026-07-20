class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr = set(nums)
        longest = 0
        
        for num in arr:
            if (num - 1) not in arr:
                curr = num
                streak = 1
                while (curr + 1 ) in arr:
                    curr += 1
                    streak += 1
                longest = max(longest, streak)
        return longest
                