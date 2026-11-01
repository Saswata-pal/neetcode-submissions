class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)< len(t):
            return ""

        t_freq={}
        for char in t:
            t_freq[char] = t_freq.get(char,0) + 1

        need=len(t_freq)
        have=0

        res_len=float('inf')
        res_indices=[-1,-1]

        window={}

        left=0
        for right in range(len(s)):
            char=s[right]
            window[char] = window.get(char,0)+1

            if char in t_freq and window[char] == t_freq[char]:
                have +=1

            while need == have:
                window_size=right-left+1
                if window_size<res_len:
                    res_len= window_size
                    res_indices=[left,right]

                left_char= s[left]
                window[left_char] -= 1

                if left_char in t_freq and window[left_char] <t_freq[left_char]:
                    have -= 1
                
                left += 1

        l,r=res_indices
        return s[l:r+1] if res_len != float('inf') else ""
