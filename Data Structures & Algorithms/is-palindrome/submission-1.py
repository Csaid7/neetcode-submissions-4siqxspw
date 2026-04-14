class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome  a strings taht are the when it has been reversed
        # two pointers r = len(s) - 1 , l = 0 
        # as the l < r , we are checking to see if the have the same letters all the way 
        # until r == l
        # we need to also use the .lower()  make sure that athe letters are the same lower case
        #  chekc to see if it is a letter/ skip
        r , l = len(s) - 1 , 0 

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            r, l = r - 1 , l + 1
        return True
                
