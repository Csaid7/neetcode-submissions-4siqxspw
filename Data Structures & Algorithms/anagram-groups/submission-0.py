class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        holder = {}

        for word in strs:
            sortedwrd = ''.join(sorted(word))
            if sortedwrd not in holder:
                holder[sortedwrd] = []
            holder[sortedwrd].append(word)
        return list(holder.values())