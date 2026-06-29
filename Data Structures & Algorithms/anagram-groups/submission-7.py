class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # way we could do this is to sort each items in the list and tehn
        # and use the sorted elemet as the key to the dictionary and the unosrted word as the value
        # create a var for the res 
        res = defaultdict(list) # default dict to take care of the  empty string 

        #Go throug the items in the strs
        for item in strs:
                # sort items
                # sortedW = sorted(item) -> turs string into a list of char ex: eat = ['a','e','t']
            sortedW = "".join(sorted(item))
                #--------------------------
                # if sortedW not in res:        Do not need this because defaultdict handles the initialization
                #     res[sortedW] = [item]
                #----------------------------
            res[sortedW].append(item)
        return list(res.values())
                # if sorted item is NOT  in  the res var 
                    #create a new key:value pair with the new sorted item as the value

            # appernf tyeh unsorted word to the key value with the sorted str
        
        #return the res