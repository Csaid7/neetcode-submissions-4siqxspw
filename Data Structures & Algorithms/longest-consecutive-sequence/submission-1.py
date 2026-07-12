class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set= set(nums)
        longest_seq = 0 

        for num in num_set:
            # check where the start is 
            # 3. Check if 'num' is the absolute START of a sequence
            # Hint: If num - 1 is NOT in num_set, then 'num' is a start!
            if (num-1) not in  num_set:
                cur_num = num
                cur_streak = 1
                while ( cur_num + 1 ) in num_set:
                    cur_num += 1
                    cur_streak += 1 
                longest_seq = max(longest_seq,cur_streak)
        return longest_seq
                    
                
