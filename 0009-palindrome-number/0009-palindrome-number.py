class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s = s[::-1]
        return s==str(x)