class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # sorting str, hash map|Dictionary 
       # using a hash map {sorteds : ["___",""]} 

       #Go through strs
            # sort index
            # store itin the hashm
        # return values of the hash map 
        res = defaultdict(list)
        for s in strs:
            sortedW = "".join(sorted(s)) # sorted = ["a","c","t"]
            res[sortedW].append(s) # {act: ["act"],opts:["stop"]}
        return list(res.values())



        

