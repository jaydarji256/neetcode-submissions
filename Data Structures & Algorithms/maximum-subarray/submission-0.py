class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        maxi = float('-inf')
        for i in range(0,n):
            total += nums[i]
            maxi = max(maxi , total)
            if total < 0:
                total = 0

        return maxi