class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #using the two pointer 
        arr = sorted(nums)
        res = []
        for i in range(len(arr)):
            # DUPLICATE SHIELD: If this number is the same as the previous one, skip it!
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            l, r = i + 1, len(arr) - 1
            while l < r:
                sum_ = arr[i] + arr[l] + arr[r]
                if sum_ == 0:
                    res.append([arr[i], arr[l], arr[r]])
                    l += 1
                    r -=1
                    while l < r and arr[l] == arr[l - 1]:
                        l += 1 
                elif sum_ > 0:
                    r -= 1
                else:
                    l += 1
        return res
        