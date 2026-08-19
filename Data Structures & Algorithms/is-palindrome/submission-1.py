class Solution:
    def isPalindrome(self, s: str) -> bool:
        straight = ""

        for char in s.lower():
            if char.isalnum():
                straight += char

        reverse = straight[::-1]

        return straight == reverse