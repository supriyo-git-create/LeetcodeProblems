class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0
        original = x

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x //=10 #this operator is called floor division operator its round up the digit example 3.5=3 and then sents 

        return original == reverse
