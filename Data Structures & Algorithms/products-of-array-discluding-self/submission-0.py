class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #creates array of the size of n 
        result = [1] * n
        #building left product
        for i in range(1,n):
            result[i] = nums[i-1] * result[i-1]

        rightprd = 1
        for i in range(n-1,-1,-1):
            result[i]*= rightprd
            rightprd*= nums[i]
            
        return result
