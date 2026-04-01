class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        holder = {}
        # example first wrd is eat

        for word in strs:
            sortedwrd = ''.join(sorted(word)) # takes eat then sort it to a e t and then joined it to aet 
            if sortedwrd not in holder:# if aet not in holder
                holder[sortedwrd] = []# creating sometyupe of key value pair
            holder[sortedwrd].append(word) # make the "eat" the key  
        return list(holder.values())