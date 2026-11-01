class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map={')':'(', '}':'{', ']':'['}

        for char in s:
            if char in bracket_map:
                #take top element if stack is not empty else push dummy
                top_el= stack.pop() if stack else "#"

                #check if the tp element matches the mappings
                if bracket_map[char] != top_el:
                    return False
            else:
                stack.append(char) 

        return len(stack) == 0