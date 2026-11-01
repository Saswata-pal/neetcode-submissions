class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result=[0] * n
        stack=[]

        for i,tem in enumerate(temperatures):
            while stack and tem> temperatures[stack[-1]]:
                prev_day= stack.pop()
                result[prev_day] = i - prev_day

            stack.append(i)
        return result