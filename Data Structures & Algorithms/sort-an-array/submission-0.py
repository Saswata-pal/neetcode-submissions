class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_num=[]
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums