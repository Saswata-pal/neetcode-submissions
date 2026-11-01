class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(left,right):
            while left<=right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l=0
        r=len(s) -1
        while l<r:
            if s[l] != s[r]:
                skip_left=check_palindrome(l+1,r)
                skip_right=check_palindrome(l,r-1)

                return skip_left or skip_right
            l += 1
            r -= 1
        return True