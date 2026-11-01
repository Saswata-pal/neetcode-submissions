class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[] #storing index and height 

        for i,h in enumerate(heights):
            start=i
            #pop elements if current bar height is less than stack's top
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                max_area=max(max_area,height*(i-index))
                start=index
            stack.append((start,h))

        for index,height in stack:
            max_area=max(max_area,height*(len(heights)-index))
        
        return max_area