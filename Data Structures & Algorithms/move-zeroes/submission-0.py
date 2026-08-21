class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp = []
        for i in range(0,n):
            if nums[i] != 0:
                temp.append(nums[i])
        k = len(temp)
        nums[:] = temp + [0]*(n-k)
