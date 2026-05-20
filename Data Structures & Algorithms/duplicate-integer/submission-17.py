class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set
        # instant look up O(1)
        # iterate through the list
        # check if the curr num is in the set
        # if it is then we have seen it and we return True else False
        seen = set()
        for i in nums:

            if i in seen:
                return True
            seen.add(i)
        return False
                