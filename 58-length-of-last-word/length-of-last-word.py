class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces and split by spaces
        words = s.strip().split()
        # Return length of the last word
        return len(words[-1])
