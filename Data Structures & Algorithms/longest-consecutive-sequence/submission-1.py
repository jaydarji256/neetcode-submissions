class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        n =len(nums)
        for i in range(0,n):
            seen.add(nums[i])

        longest = 0

        for num in seen:
            if num-1 not in seen:
                x = num
                count = 1
                while x+1 in seen:
                    count += 1
                    x+=1
                longest = max(longest , count)

        return longest