class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0

        for n in num_set:
            if (n-1) not in num_set:
                curr_num = n
                curr_streak = 1
            
                while (curr_num + 1) in num_set:
                    curr_num+=1
                    curr_streak+=1
            
                longest= max(curr_streak,longest)

        return longest