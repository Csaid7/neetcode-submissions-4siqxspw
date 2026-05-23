class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers
        #r,l ex: [0,1,2,3,4] target = 7
        #r = 4 l = 0
        # look for sum  ==  4 + 0 < 7
        # since sum < target move l pointer up 
        # else move right pointer down 
        r , l = len(numbers) - 1, 0

        while l < r:
            
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1,r + 1]
        return []
                
