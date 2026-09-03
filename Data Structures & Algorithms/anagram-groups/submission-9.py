class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map = {key : value}
        """
        {act :[act,act],
        otsp : [pots,tops,stop],
        aht : [hat]
                
         }
        """
        res = defaultdict(list)

        
        for i in strs:

            sortedW = "".join(sorted(i))

            res[sortedW].append(i)
        return list(res.values())