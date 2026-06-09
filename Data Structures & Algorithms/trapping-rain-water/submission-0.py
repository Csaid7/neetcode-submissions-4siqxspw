class Solution:
    def trap(self, height: List[int]) -> int:
        #pref max ,pre
        n = len(height)
        if n == 0:
            return 0
        pre_max = [0] * n
        suff_max = [0] * n 
        """
        0 2 0 3 1 0 1 3 2 1 
        [][][][][][][][][][]
        pre_max[0] = 0
        pre[1] = max( 0 , 2) = 2
        pre[2] = max(2,0) = 2
        """
        pre_max[0] = height[0]
        for i in range(1,n):
            pre_max[i] = max(pre_max[i-1], height[i])

        suff_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suff_max[i] = max(suff_max[i+1], height[i])
        
        res = 0
        for i in range(n):
            res += min(pre_max[i], suff_max[i]) - height[i]
            
        return res 