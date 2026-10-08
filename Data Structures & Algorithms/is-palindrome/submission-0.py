class Solution:
    def isPalindrome(self, s: str) -> bool:
         s=[c.lower() for c in s if c.isalnum()]
         left=0
         right=len(s)-1
         
         while left<right:
            if s[left]==s[right]:
                left=left+1
                right=right-1
            else:
                return False
         return True

