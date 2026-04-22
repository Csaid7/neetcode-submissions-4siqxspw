class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #BRUTE FORCE
        """
        Have two pointers
        for each iteration we are going to calculate the area by getting the wdith
        width : distance between pointer r and l
        lenght: min number between height[l] and height[r]
        store it into res var ( keep the max number between the biggest area and new area)
        """
        res = 0 

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                # area : r,l indexs to calculate the width of the container
                # min() : is to calculate the height by getting the shortest wall between the two
                
                area = (r - l) * min(heights[l], heights[r])
                res = max(res, area)
        return res
    