class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # var to hold max area
        maxArea = 0
        l, r = 0 , len(heights) - 1 
        while l < r:
            # check for the smallest height and that will be the length
                # by doing some sort of l = min(height[l], height[r])
            h = min(heights[l], heights[r])
            # calculat ethe width 
                # doing some sort of w = r - l
            w = r - l
            # calculate teh are :
                # area = l * r
            area = h * w
            #maxArea = max(MaxArea, area)
            maxArea = max(maxArea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea