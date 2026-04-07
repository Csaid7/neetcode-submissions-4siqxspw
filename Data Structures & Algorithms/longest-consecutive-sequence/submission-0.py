class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        use a set() to get rid of the duplicate
        check to see if the num at the curr index is the start of a sequence
        2 - check to see if 1 is in the set() 
        if it's in the set start the sequence and check to see if 3 is in the set 
        20- check if start of sequence, is 21 in the set, if not we will set the length to 1
        """
        numSet= set(nums) # creates a new array with no duplicates [[2],20,4,10,3,5]
        longest = 0 

        for num in numSet: # [2]
            #check if it's the start of a sequence
            if ( num - 1) not in numSet: # [1 in numSet] -> no (Start of a sequence)
                length = 1 #[ set length = 1]
                while (num + length) in numSet: # [2 +1] in numSet -> yes
                    length += 1 # increment length
                longest = max( length, longest)
        return longest

    