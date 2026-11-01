class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for indx,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],indx]
            seen[num] = indx
