class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      anagram =defaultdict(list)

        
      for word in strs:
         count =[0]*26
         for c in word:
            count[ord(c) -ord('a')] += 1
            # dictionary keys must be immutable(unchangeable)
            # list are mutable  
         anagram[tuple(count)].append(word)
      return list(anagram.values())
          
