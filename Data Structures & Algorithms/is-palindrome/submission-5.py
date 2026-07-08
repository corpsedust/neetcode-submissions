class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        s = s.replace(" ", "").lower()
        s = ''.join(c for c in s if c.isalnum())
        second = len(s) - 1
        first = 0

        s.replace(" ", "").lower()
        while second != first and first < second:
            
            if s[first].lower() == s[second].lower():
                first = first + 1
                second -= 1
            else:
                return False

        

        return True