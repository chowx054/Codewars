class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        while sorted(s) == sorted(t):
            return True
        return False