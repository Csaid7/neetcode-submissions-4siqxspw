class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
         # anangram is string that contains the same char( has to be the same length)
         
         # sort the array and comapre if it is the same right but time complexity is O(nlogn)
         # Hash map where count the number of letters in each string
         # and see if it has the same number of letters then it is a anagram
         # Example:
         # racecar and carrace
         # each have r:2 a:2 c:2 e:2
         if len(s) != len(t):
            return False
         count_s = {}
         count_t = {}
         for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i],0) + 1 
            count_t[t[i]] = count_t.get(t[i],0) + 1
         return count_s == count_t
