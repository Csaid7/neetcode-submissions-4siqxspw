class Solution:
    def maxArea(self, heights: List[int]) -> int:

        """
        Efficient solution
        two pointers : one at beginning and one at the end of the array 
        calculate the area: w( distance between the two pointers) * h( min num between height[l||r])
        if pointer to r is smaller than l move r pointer to left vice versa
        """

        l, r = 0, len(heights) - 1
        res = 0 
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res,area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res

