class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting words and grouping them

        res = defaultdict(list)
        for i in strs:
            srtd = " ".join(sorted(i))
            res[srtd].append(i)
        return list(res.values())
        