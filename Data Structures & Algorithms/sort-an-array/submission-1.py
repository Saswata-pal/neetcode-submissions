class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merged(left,right):
            sorted_arr=[]
            i=j=0
            while i < len(left) and j<len(right):
                if left[i]<right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])

            return sorted_arr
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums)//2
            left_half=nums[:mid]
            right_half=nums[mid:]

            left_sorted=merge_sort(left_half)
            right_sorted=merge_sort(right_half)

            return merged(left_sorted,right_sorted)
        
        return merge_sort(nums)
        