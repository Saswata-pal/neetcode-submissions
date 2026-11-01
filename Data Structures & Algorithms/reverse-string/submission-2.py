class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # tmp = []
        # for i in range(len(s)-1,-1,-1):
        #     tmp.append(s[i])
        # for i in range(len(s)):
        #     s[i]= tmp[i]
        def reversee(l,r):
            if l<r:
                reversee(l+1,r-1)
                s[l],s[r] = s[r],s[l]
        reversee(0,len(s)-1)