class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pInd , nInd = 0,1
        for i in range(0,n):
            if nums[i] >= 0:
                result[pInd] = nums[i]
                pInd += 2

            else:
                result[nInd] = nums[i]
                nInd += 2

        return result  